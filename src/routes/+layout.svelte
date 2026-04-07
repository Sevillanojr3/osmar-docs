<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/favicon.png" />
</svelte:head>

<!-- Fixed background on ALL sections -->
<div class="pointer-events-none fixed inset-0" style="z-index:0;background:url(/images/fondo-sm.webp) center/cover no-repeat fixed;opacity:0.06;"></div>

<div style="position:relative;z-index:1;">
	{@render children()}
</div>
