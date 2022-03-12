import Button from "./button/button.vue"
import Tabs from "./tabs/tabs.vue"
import Tab from "./tabs/tab.vue"
import Select from "./select/index.vue"
import Option from "./option/index.vue"
import Menu from "./menu/menu.vue"
import Checkbox from "./checkbox/checkbox.vue"
import Collapse from "./collapse/collapse"
import Dialog from "./dialog/dialog.vue"

import { App } from "vue"

const components = {
  Button,
  Tabs,
  Option,
  Tab,
  Select,
  Menu,
  Checkbox,
  Collapse,
  Dialog
}

export default {
  install(app: App) {
    for (let [key, value] of Object.entries(components)) {
      app.component(`calc-${key.toLocaleLowerCase()}`, value)
    }
  }
}
