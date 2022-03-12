import type { ComponentPropsOptions, SetupContext } from "vue"

export function defineHooks<P, R>(
  _: ComponentPropsOptions<P>,
  setup: (props: P, context: SetupContext) => R
) {
  return setup
}
