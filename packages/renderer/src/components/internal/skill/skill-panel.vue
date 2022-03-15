<script lang="tsx">
	import { defineComponent, onMounted, reactive, ref, computed } from "vue"
	import SkillIcon from "./skill-icon.vue"
	export default defineComponent({
		name: "skill-panel",
		components: { SkillIcon },
		props: {
		},
		setup(props, { emit }) {
			
			const skills = reactive([
				{
					lv: 1,
					sks: [
						{ id: 1, name: '冰结师皮甲专精', col: 1, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 2, name: '不死之身', col: 2, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 3, name: '黑暗之眼', col: 3, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 4, name: '基础防具精通', col: 4, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7001, name: '魔法水球', col: 5, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7002, name: '魔法旋风', col: 7, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 5,
					sks: [
						{ id: 7003, name: '擒拿掌', col: 4, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7004, name: '魔球连射', col: 7, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 10,
					sks: [
						{ id: 7005, name: '幽冥火', col: 3, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7006, name: '瞬移', col: 6, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7007, name: '旋火盾', col: 8, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 15,
					sks: [
						{ id: 7008, name: '', col: 4, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7009, name: '', col: 7, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7010, name: '', col: 9, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 20,
					sks: [
						{ id: 7011, name: '', col: 5, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 25,
					sks: [
						{ id: 7012, name: '', col: 4, sp: 0, jt: 1, max: 1, default: 1  },
						{ id: 7013, name: '', col: 6, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7014, name: '', col: 8, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 30,
					sks: [
						{ id: 7015, name: '', col: 3, sp: 0, jt: 1, max: 1, default: 1, before: [7012] },
						{ id: 7016, name: '', col: 5, sp: 0, jt: 1, max: 1, default: 1, before: [7012] },
						{ id: 7017, name: '', col: 8, sp: 0, jt: 1, max: 1, default: 1, before: [7014] },
						{ id: 7018, name: '', col: 9, sp: 0, jt: 1, max: 1, default: 1, before: [7010] },
					]
				},
				{
					lv: 35,
					sks: [
						{ id: 7019, name: '', col: 3, sp: 0, jt: 1, max: 1, default: 1, before: [7015] },
						{ id: 7020, name: '', col: 5, sp: 0, jt: 1, max: 1, default: 1, before: [7016] },
					]
				},
				{
					lv: 40,
					sks: [
						{ id: 7021, name: '', col: 5, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 45,
					sks: [
						{ id: 7022, name: '', col: 4, sp: 0, jt: 1, max: 1, default: 1, before: [7021] },
						{ id: 7023, name: '', col: 6, sp: 0, jt: 1, max: 1, default: 1, before: [7021] },
					]
				},
				{
					lv: 50,
					sks: [
						{ id: 7024, name: '', col: 6, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7025, name: '', col: 7, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 60,
					sks: [
						{ id: 7026, name: '', col: 6, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 70,
					sks: [
						{ id: 7027, name: '', col: 5, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7028, name: '', col: 7, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7029, name: '', col: 9, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 80,
					sks: [
						{ id: 7030, name: '', col: 7, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7031, name: '', col: 9, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 90,
					sks: [
						{ id: 7032, name: '', col: 6, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7033, name: '', col: 8, sp: 0, jt: 1, max: 1, default: 1 },
					]
				},
				{
					lv: 100,
					sks: [
						{ id: 7034, name: '', col: 5, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7035, name: '', col: 7, sp: 0, jt: 1, max: 1, default: 1 },
						{ id: 7036, name: '', col: 8, sp: 0, jt: 1, max: 1, default: 1 }
					]
				},
			])
			
			const drawData = computed(() => {
				let ss = [];
				let data = [];
				for(var i = 0; i < skills.length; i++) {
					var group = skills[i]
					for(var s of group.sks) {
						if(s.before) {
							for(var bb of s.before) {
								var b = ss.find(x => x.id == bb);
								if(b) {
									data.push({
										ey: i,
										ex: s.col,
										sy: b.y,
										sx: b.col,
										s,
										b
									});
								}
							}
						}
						s.y = i;
						ss.push(s);
					}
				}
				return data;
			});
			
			function draw() {
				let canvas = document.getElementById('canvas-for-skill-back');
				let ctx = canvas.getContext("2d");
				canvas.width = 848;
				canvas.height = skills.length * 100;
				
				for(var i = 0; i < skills.length; i++) {
					ctx.fillStyle = i % 2 == 0 ? 'rgba(0, 0, 0, 0.3)' : 'rgba(30, 30, 30, 0.3)';
					ctx.fillRect(0, i * 100, canvas.width, 100);
				}
				ctx.fillStyle="#593D22";
				for(var item of drawData.value) {
					let x = (item.sx - 1) * 75 + 30 + 27;
					let y = item.sy * 100 + 90;
					let h = (item.ey - item.sy) * 100 - 86;
					let w = (item.ex - item.sx) * 75;
					
					ctx.fillRect(x, y, 6, h / 2);
					ctx.fillRect(x, y + h / 2, w, 6);
					ctx.fillRect(x + w, y + h / 2, 6, h / 2);
					
					ctx.beginPath();
					ctx.moveTo(x + w - 5, y + h);
					ctx.lineTo(x + w + 11, y + h);
					ctx.lineTo(x + w + 3, y + h + 6);
					ctx.closePath();
					ctx.fill();
				}
				
			}
			
			onMounted(draw)
			
			return () => {
				return (
					<div class="skill-panel">
						<el-scrollbar>
							<canvas id="canvas-for-skill-back"></canvas>
							{ skills.map(skm =>
								<div class="skills-group">
									<div class="lv-tips">{skm.lv % 10 == 0 || skm.lv == 1 ? skm.lv : ''}</div>
									{ skm.sks.map((s, i) => <skill-icon class="skill-item" style={'left: ' + ((s.col - 1) * 75 + 30) + 'px'}></skill-icon>) }
								</div>)
							}
						</el-scrollbar>
					</div>
				)
			}
		}
	})
</script>
<style scoped lang="scss">
.skill-panel {
	height: 1600px;
	position: relative;
	
	
	.skills-group {
		height: 100px;
		position: relative;
		
		.lv-tips {
			padding: 10px;
			position: absolute;
		}
		
		.skill-item {
			position: absolute;
			top: 10px;
			z-index: 5;
		}
	}
	
	#canvas-for-skill-back {
		float: left;
	}
}
</style>