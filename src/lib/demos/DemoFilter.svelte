<script>
  import { demoFilter } from "$lib/urtService";

  function resetFilter() {
    demoFilter.set("");
  }

  function reloadDemos() {
    //TODO
  }
</script>

<input bind:value={$demoFilter} placeholder="Demo name" />
{#if $demoFilter}
  <button on:click={resetFilter}>X</button>
{/if}
<button on:click={reloadDemos}>♻️</button>
