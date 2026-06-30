type Typewriter = {
  push: (text: string) => void
  drain: () => Promise<void>
  stop: () => void
}

export function createTypewriter(onText: (text: string) => void): Typewriter {
  let queue = ""
  let timerId: number | null = null
  const drainResolvers: Array<() => void> = []

  const resolveDrain = () => {
    while (drainResolvers.length > 0) {
      drainResolvers.shift()?.()
    }
  }

  const stopTimer = () => {
    if (timerId !== null) {
      window.clearInterval(timerId)
      timerId = null
    }
  }

  const tick = () => {
    if (!queue) {
      stopTimer()
      resolveDrain()
      return
    }

    const chunkSize = queue.startsWith("\n") ? 1 : Math.min(queue.length, 4)
    const nextText = queue.slice(0, chunkSize)
    queue = queue.slice(chunkSize)
    onText(nextText)
  }

  const start = () => {
    if (timerId === null) {
      timerId = window.setInterval(tick, 24)
    }
  }

  return {
    push(text: string) {
      queue += text
      start()
    },
    drain() {
      if (!queue && timerId === null) {
        return Promise.resolve()
      }

      return new Promise<void>((resolve) => {
        drainResolvers.push(resolve)
        start()
      })
    },
    stop() {
      queue = ""
      stopTimer()
      resolveDrain()
    },
  }
}
