<script>
	import CategoryThumbnail from '../../components/CategoryThumbnail.svelte';
	let categories;
</script>

<h1 class="text-center mt-4">Categorias</h1>
<div class="row mt-4">
	{#each categories as category}
		<div class="col">
			<CategoryThumbnail {category} />
		</div>
	{:else}
		<p>No categories</p>
	{/each}
</div>
