<script context="module">
	/** @type {import('@sveltejs/kit').Load} */
	export async function load({ page }) {
		const url = `http://localhost:1337/api/categorias`;
		const res = await fetch(url);
		const categories = await res.json();
		if (res.ok) {
			return {
				props: {
					categories: categories.data
				}
			};
		}

		return {
			status: res.status,
			error: new Error(res.statusText)
		};
	}
</script>

<script>
	import CategoryThumbnail from '../../components/CategoryThumbnail.svelte';
	export let categories;
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
