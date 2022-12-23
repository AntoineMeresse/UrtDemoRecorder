<script lang="ts">
  import { demoNameFilter } from "$lib/urtService";
  export let demoName: string;
</script>

{#if !$demoNameFilter || demoName.includes($demoNameFilter)}
  <div>
    <p>{demoName}</p>
  </div>
{/if}
