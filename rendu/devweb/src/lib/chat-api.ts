import axios, { type AxiosProgressEvent } from "axios"

const CHAT_ENDPOINT = import.meta.env.VITE_TECHCORP_API_URL ?? "/api/generate"
const MODEL = "techcorp-financial"

type GenerateChunk = {
  response?: string
  done?: boolean
  error?: string
}

type StreamOptions = {
  prompt: string
  signal?: AbortSignal
  onToken: (token: string) => void
}

function readProgressText(progressEvent: AxiosProgressEvent) {
  const target = progressEvent.event?.currentTarget as XMLHttpRequest | null

  return typeof target?.responseText === "string" ? target.responseText : ""
}

function parseChunk(line: string) {
  return JSON.parse(line) as GenerateChunk
}

export async function streamChatResponse({
  prompt,
  signal,
  onToken,
}: StreamOptions) {
  let readLength = 0
  let buffer = ""

  const consume = (text: string) => {
    const nextText = text.slice(readLength)
    readLength = text.length
    buffer += nextText

    const lines = buffer.split(/\r?\n/)
    buffer = lines.pop() ?? ""

    for (const line of lines) {
      if (!line.trim()) {
        continue
      }

      const chunk = parseChunk(line)

      if (chunk.error) {
        throw new Error(chunk.error)
      }

      if (chunk.response) {
        onToken(chunk.response)
      }
    }
  }

  const flush = () => {
    if (!buffer.trim()) {
      return
    }

    const chunk = parseChunk(buffer)

    if (chunk.error) {
      throw new Error(chunk.error)
    }

    if (chunk.response) {
      onToken(chunk.response)
    }

    buffer = ""
  }

  const response = await axios.post<string>(
    CHAT_ENDPOINT,
    {
      model: MODEL,
      prompt,
      stream: true,
      keep_alive: -1,
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
      responseType: "text",
      signal,
      transformResponse: [(data) => data],
      onDownloadProgress: (progressEvent) => {
        const responseText = readProgressText(progressEvent)

        if (responseText.length > readLength) {
          consume(responseText)
        }
      },
    }
  )

  if (typeof response.data === "string" && response.data.length > readLength) {
    consume(response.data)
  }

  flush()
}
