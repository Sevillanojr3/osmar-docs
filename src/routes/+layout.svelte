<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/favicon.png" />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
</svelte:head>

<!-- Fixed background on ALL sections -->
<div class="pointer-events-none fixed inset-0" style="z-index:0;background:url(/images/fondo-sm.jpg) center/cover no-repeat fixed;opacity:0.06;"></div>

<div style="position:relative;z-index:1;">
	{@render children()}
</div>
