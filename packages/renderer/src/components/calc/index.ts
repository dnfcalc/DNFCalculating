import Button from "./button/index.vue"
import Tabs from "./tabs/index.vue"
import Tab from "./tab.vue"
import Select from "./select/index.vue"
import Option from "./option/index.vue"
import Menu from "./menu/menu.vue"
import Checkbox from "./checkbox/index.vue"
import Collapse from "./collapse/collapse"
import Dialog from "./dialog/index.vue"
import Tooltip from "./tooltip/index.vue"

import type { App } from "vue"

export const components = {
  Button,
  Tabs,
  Option,
  Tab,
  Select,
  Menu,
  Checkbox,
  Collapse,
  Dialog,
  Tooltip
}

export type CalcComponents = typeof components

export function install(app: App) {
  for (let [key, value] of Object.entries(components)) {
    app.component(`calc-${key.toLocaleLowerCase()}`, value)
  }
}

export default components
