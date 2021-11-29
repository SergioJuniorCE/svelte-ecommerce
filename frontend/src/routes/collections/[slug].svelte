<script context="module">
	export async function load({ page }) {
		const slug = page.params.slug;
		const url = `http://localhost:1337/categories/${slug}`;
		const res = await fetch(url);
		const category = await res.json();
		return {
			props: {
				category
			}
		};
	}
</script>
<script>
	import ProductThumbnail from '../../components/ProductThumbnail.svelte';
	export let category;
</script>

<div class="text-center">
	<h1 class="mt-4">{category.title}</h1>
</div>


<div class="row">
	{#each category.products as product}
		<div class="col">
			<ProductThumbnail product={product}/>
		</div>
	{:else}
		<p>asd</p>
	{/each}
</div>
