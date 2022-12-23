<script>
  import { demoNameFilter, loadDemosFiles } from "$lib/urtService";

  function resetFilter() {
    demoNameFilter.set("");
  }
</script>

<input bind:value={$demoNameFilter} placeholder="Demo name" />

{#if $demoNameFilter}
  <button on:click={resetFilter}>X</button>
{/if}

<button on:click={loadDemosFiles}>♻️</button>
