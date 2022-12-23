<script lang="ts">
  const links = [
    { name: "Home", url: "/" },
    { name: "Maps", url: "/maps" },
    { name: "Demos", url: "/demos" },
    { name: "Settings", url: "/settings" },
  ];
</script>

<nav>
  {#each links as link}
    <a href={link.url}>{link.name}</a>
  {/each}
</nav>

<style>
  nav {
    display: flex;
    justify-content: space-between;
  }
</style>
