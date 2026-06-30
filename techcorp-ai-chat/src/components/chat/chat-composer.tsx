import { useRef, type FormEvent } from "react"
import { Loader2, SendHorizontal } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { useAutoResizeTextarea } from "@/hooks/use-auto-resize-textarea"

type ChatComposerProps = {
  input: string
  isStreaming: boolean
  onInputChange: (input: string) => void
  onSubmit: () => void
}

export function ChatComposer({
  input,
  isStreaming,
  onInputChange,
  onSubmit,
}: ChatComposerProps) {
  const textareaRef = useRef<HTMLTextAreaElement | null>(null)

  useAutoResizeTextarea(textareaRef, input, { maxHeight: 180 })

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    onSubmit()
  }

  return (
    <form
      className="pointer-events-none fixed inset-x-0 bottom-0 z-10 bg-gradient-to-t from-background via-background to-background/0 px-3 pb-3 pt-12 sm:px-6 sm:pb-5"
      onSubmit={handleSubmit}
    >
      <div className="pointer-events-auto mx-auto flex max-w-3xl items-end gap-2 rounded-3xl border bg-background p-2 shadow-lg shadow-black/5">
        <Textarea
          ref={textareaRef}
          value={input}
          rows={1}
          placeholder="Message TechCorp..."
          disabled={isStreaming}
          className="max-h-[180px] min-h-10 resize-none border-0 bg-transparent px-3 py-2.5 shadow-none focus-visible:ring-0"
          onChange={(event) => onInputChange(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter" && !event.shiftKey) {
              event.preventDefault()
              event.currentTarget.form?.requestSubmit()
            }
          }}
        />
        <Button
          type="submit"
          size="icon"
          className="mb-1 rounded-full"
          disabled={!input.trim() || isStreaming}
          aria-label="Send message"
        >
          {isStreaming ? (
            <Loader2 className="animate-spin" />
          ) : (
            <SendHorizontal />
          )}
        </Button>
      </div>
    </form>
  )
}
