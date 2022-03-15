<script lang="tsx">
	import { defineComponent, reactive } from "vue"
	export default defineComponent({
		name: "skill-icon",
		components: {  },
		props: {
			
		},
		setup(props, { emit }) {
			return () => {
				return (
					<div class="skill-icon"></div>
				)
			}
		}
	})
</script>
<style scoped lang="scss">
.skill-icon {
	display: inline-block;
	width: 60px;
	height: 80px;
	border: 1px solid transparent;
	border-radius: 5px;
	background-color: #000;
	cursor: pointer;
	
	&:hover {
		border-color: #64ADD0;
	}
}

</style>