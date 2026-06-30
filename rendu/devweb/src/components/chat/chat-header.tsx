import { cn } from "@/lib/utils"

type ChatHeaderProps = {
  isStreaming: boolean
}

export function ChatHeader({ isStreaming }: ChatHeaderProps) {
  return (
    <header className="flex h-14 shrink-0 items-center justify-between px-4 sm:px-6">
      <div className="min-w-0">
        <h1 className="truncate text-sm font-semibold">TechCorp</h1>
        <p className="truncate text-xs text-muted-foreground">
          Financial model
        </p>
      </div>
      <div
        className={cn(
          "size-2 rounded-full",
          isStreaming ? "bg-emerald-500" : "bg-muted-foreground/40"
        )}
        aria-hidden="true"
      />
    </header>
  )
}
