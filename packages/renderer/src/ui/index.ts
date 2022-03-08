import Button from "./button/button"
import Tabs from "./tabs/tabs"
import Tab from "./tabs/tab"
import Select from "./select"
import Option from "./option"
import Menu from "./menu/menu"
import Checkbox from "./checkbox/checkbox"
import Collapse from "./collapse/collapse"

import { App } from "vue"

const components = [Button, Tabs, Tab, Select, Option, Menu, Checkbox, Collapse]

export default {
    install(app: App) {
        components.forEach(c => {
            app.component(c.name.replace("i-", "calc-"), c)
        })
    }
}
