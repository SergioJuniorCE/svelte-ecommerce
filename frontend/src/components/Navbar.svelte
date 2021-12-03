<script context="module">
	export async function load({ page }) {
		return {
			props: {
			}
		};
	}
</script>
<script>
	import NavItem from './NavItem.svelte';
	let cart_amount = 0
</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
	<div class="container">
		<a class="navbar-brand" href="/">Brand</a>
		<button
			class="navbar-toggler"
			type="button"
			data-bs-toggle="collapse"
			data-bs-target="#navbar"
			aria-controls="navbar"
			aria-expanded="false"
			aria-label="Toggle navigation"
		>
			<span class="navbar-toggler-icon" />
		</button>
		<div class="collapse navbar-collapse" id="navbar">
			<ul class="navbar-nav me-auto mb-2 mb-lg-0">
				<NavItem href="/about" title="About" />
				<NavItem href="/categorias" title="Todas las categorias" />
				<li class="nav-item dropdown">
					<a
						class="nav-link dropdown-toggle"
						href="#!"
						id="navbarDropdown"
						role="button"
						data-bs-toggle="dropdown"
						aria-expanded="false"
					>
						Dropdown
					</a>
					<ul class="dropdown-menu" aria-labelledby="navbarDropdown">
						<li><a class="dropdown-item" href="#!">Action</a></li>
						<li><a class="dropdown-item" href="#!">Another action</a></li>
						<li><hr class="dropdown-divider" /></li>
						<li><a class="dropdown-item" href="#!">Something else here</a></li>
					</ul>
				</li>
			</ul>
			<div class="d-flex">
				<button class="btn btn-outline-dark"><i class="fas fa-shopping-bag" />&nbsp; carrito ( {cart_amount} )</button>
			</div>
		</div>
	</div>
</nav>
