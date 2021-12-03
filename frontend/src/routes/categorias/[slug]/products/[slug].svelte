<script context="module">
	export async function load({ page }) {
		const slug = page.params.slug;
		// const url = `http://localhost:1337/products/${slug}`;
		// const res = await fetch(url);
		// const category = await res.json();
		return {
			props: {
				// category,
        slug
			}
		};
	}
</script>
<script>
  export let slug
</script>

<h1>{slug}</h1>
<p>{slug}</p>