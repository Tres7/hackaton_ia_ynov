import { ChatComposer } from "@/components/chat/chat-composer"
import { ChatHeader } from "@/components/chat/chat-header"
import { ChatThread } from "@/components/chat/chat-thread"
import { useStreamingChat } from "@/hooks/use-streaming-chat"

export function App() {
  const { input, isStreaming, messages, sendMessage, setInput } =
    useStreamingChat()

  return (
    <main className="flex h-svh overflow-hidden bg-background text-foreground">
      <section className="mx-auto flex h-full w-full max-w-4xl flex-col bg-background">
        <ChatHeader isStreaming={isStreaming} />
        <ChatThread messages={messages} />
        <ChatComposer
          input={input}
          isStreaming={isStreaming}
          onInputChange={setInput}
          onSubmit={sendMessage}
        />
      </section>
    </main>
  )
}

export default App
