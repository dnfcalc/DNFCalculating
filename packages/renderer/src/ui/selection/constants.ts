/**
 * @Author: Kritsu
 * @Date:   2021/11/16 19:24:26
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:50:15
 */
export const AciveSymbol = Symbol("[i-selection]active")

export const InitSymbol = Symbol("[i-selection]init")

export const ModelValueSymbol = Symbol("[i-selection]model-value")

export const AciveClassSymbol = Symbol("[i-selection]active-class")

export const ItemLabelSymbol = Symbol("[i-selection]label")
export const ItemOptionsSymbol = Symbol("[i-selection]options")

export const ChangeActiveSymbol = Symbol("[i-selection]change-active")

export interface Option {
    value: any
    key: string
}
