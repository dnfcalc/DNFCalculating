<template>{{ adventureinfo }}</template>
<script lang="ts" setup>
import { useBasicInfoStore } from '../../store'
const basicInfoState = useBasicInfoStore()
await basicInfoState.get_basic_info()
const adventureinfo = basicInfoState.adventureinfo
</script>
