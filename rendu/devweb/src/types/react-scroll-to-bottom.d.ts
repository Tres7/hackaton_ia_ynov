declare module "react-scroll-to-bottom" {
  import type { ComponentType, ReactNode } from "react"

  type ScrollerState = {
    maxValue: number
    minValue: number
    offsetHeight: number
    scrollHeight: number
    scrollTop: number
  }

  type ScrollToBottomProps = {
    checkInterval?: number
    children?: ReactNode
    className?: string
    debounce?: number
    debug?: boolean
    followButtonClassName?: string
    initialScrollBehavior?: "auto" | "smooth"
    mode?: "bottom" | "top"
    nonce?: string
    scroller?: (state: ScrollerState) => number
    scrollViewClassName?: string
  }

  const ScrollToBottom: ComponentType<ScrollToBottomProps>

  export default ScrollToBottom
}
