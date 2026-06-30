import { useEffect, useRef, useState } from "react"

import type { ChatMessage } from "@/components/chat/types"
import { streamChatResponse } from "@/lib/chat-api"
import { createTypewriter } from "@/lib/typewriter"

function createId() {
  return crypto.randomUUID()
}

export function useStreamingChat() {
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [input, setInput] = useState("")
  const [isStreaming, setIsStreaming] = useState(false)
  const abortRef = useRef<AbortController | null>(null)

  useEffect(() => {
    return () => abortRef.current?.abort()
  }, [])

  const updateAssistantMessage = (
    messageId: string,
    updater: (message: ChatMessage) => ChatMessage
  ) => {
    setMessages((currentMessages) =>
      currentMessages.map((message) =>
        message.id === messageId ? updater(message) : message
      )
    )
  }

  const sendMessage = async () => {
    const prompt = input.trim()

    if (!prompt || isStreaming) {
      return
    }

    const userMessage: ChatMessage = {
      id: createId(),
      role: "user",
      content: prompt,
      status: "done",
    }
    const assistantMessage: ChatMessage = {
      id: createId(),
      role: "assistant",
      content: "",
      status: "streaming",
    }
    const controller = new AbortController()
    const typewriter = createTypewriter((text) => {
      updateAssistantMessage(assistantMessage.id, (message) => ({
        ...message,
        content: message.content + text,
      }))
    })

    abortRef.current = controller
    setMessages((currentMessages) => [
      ...currentMessages,
      userMessage,
      assistantMessage,
    ])
    setInput("")
    setIsStreaming(true)

    try {
      await streamChatResponse({
        prompt,
        signal: controller.signal,
        onToken: (token) => {
          typewriter.push(token)
        },
      })
      await typewriter.drain()

      updateAssistantMessage(assistantMessage.id, (message) => ({
        ...message,
        status: "done",
      }))
    } catch (error) {
      if (controller.signal.aborted) {
        typewriter.stop()
        updateAssistantMessage(assistantMessage.id, (message) => ({
          ...message,
          status: "done",
        }))
        return
      }

      typewriter.stop()
      const errorMessage =
        error instanceof Error
          ? error.message
          : "The model did not return a readable response."

      updateAssistantMessage(assistantMessage.id, (message) => ({
        ...message,
        content: message.content || `Request failed: ${errorMessage}`,
        status: "error",
      }))
    } finally {
      if (abortRef.current === controller) {
        abortRef.current = null
      }

      setIsStreaming(false)
    }
  }

  const stopStreaming = () => {
    abortRef.current?.abort()
  }

  return {
    input,
    isStreaming,
    messages,
    sendMessage,
    setInput,
    stopStreaming,
  }
}
