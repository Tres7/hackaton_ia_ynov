import { useLayoutEffect, type RefObject } from "react"

type AutoResizeOptions = {
  maxHeight: number
}

export function useAutoResizeTextarea(
  textareaRef: RefObject<HTMLTextAreaElement | null>,
  value: string,
  { maxHeight }: AutoResizeOptions
) {
  useLayoutEffect(() => {
    const textarea = textareaRef.current

    if (!textarea) {
      return
    }

    textarea.style.height = "0px"
    textarea.style.height = `${Math.min(textarea.scrollHeight, maxHeight)}px`
  }, [maxHeight, textareaRef, value])
}
