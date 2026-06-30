import { Bot, Loader2, UserRound } from "lucide-react"
import ScrollToBottom from "react-scroll-to-bottom"

import type { ChatMessage } from "@/components/chat/types"
import { cn } from "@/lib/utils"

type ChatThreadProps = {
  messages: ChatMessage[]
}

function EmptyThread() {
  return (
    <div className="flex h-full items-center justify-center">
      <div className="flex max-w-xl flex-col items-center gap-4 text-center">
        <div className="flex size-11 items-center justify-center rounded-full border bg-background shadow-sm">
          <Bot className="size-5" />
        </div>
        <div className="space-y-2">
          <h2 className="text-2xl font-semibold tracking-tight">
            How can I help with finance today?
          </h2>
          <p className="text-sm text-muted-foreground">
            Ask about ratios, cash flow, working capital, or financial analysis.
          </p>
        </div>
      </div>
    </div>
  )
}

function UserMessage({ message }: { message: ChatMessage }) {
  return (
    <div className="flex max-w-[min(82%,38rem)] items-start gap-2">
      <div className="rounded-2xl bg-emerald-600 px-4 py-2.5 text-sm leading-6 text-white shadow-sm break-words whitespace-pre-wrap">
        {message.content}
      </div>
      <div className="mt-0.5 hidden size-7 shrink-0 items-center justify-center rounded-full bg-emerald-600 text-white sm:flex">
        <UserRound className="size-4" />
      </div>
    </div>
  )
}

function AssistantMessage({ message }: { message: ChatMessage }) {
  return (
    <>
      <div className="mt-0.5 hidden size-7 shrink-0 items-center justify-center rounded-full border bg-background sm:flex">
        <Bot className="size-4" />
      </div>
      <div
        className={cn(
          "max-w-full pt-0.5 text-[0.95rem] leading-7 text-foreground break-words whitespace-pre-wrap",
          message.status === "error" && "text-destructive"
        )}
      >
        {message.content}
        {message.status === "streaming" && (
          <span className="ml-1 inline-flex translate-y-0.5">
            <Loader2 className="size-3.5 animate-spin text-muted-foreground" />
          </span>
        )}
      </div>
    </>
  )
}

function ChatMessageItem({ message }: { message: ChatMessage }) {
  return (
    <article
      className={cn(
        "flex w-full gap-3",
        message.role === "user" ? "justify-end" : "justify-start sm:-ml-9"
      )}
    >
      {message.role === "user" ? (
        <UserMessage message={message} />
      ) : (
        <AssistantMessage message={message} />
      )}
    </article>
  )
}

export function ChatThread({ messages }: ChatThreadProps) {
  return (
    <ScrollToBottom
      checkInterval={17}
      className="min-h-0 flex-1"
      debounce={17}
      followButtonClassName="hidden"
      initialScrollBehavior="auto"
      mode="bottom"
      scroller={() => Infinity}
      scrollViewClassName="min-h-full overscroll-contain px-4 pb-32 pt-4 [overflow-anchor:none] sm:px-6"
    >
      {messages.length === 0 ? (
        <EmptyThread />
      ) : (
        <div className="mx-auto flex w-full max-w-3xl flex-col gap-7">
          {messages.map((message) => (
            <ChatMessageItem key={message.id} message={message} />
          ))}
        </div>
      )}
    </ScrollToBottom>
  )
}
