<script lang="ts">
  import { demoFilter } from "$lib/urtService";
  export let demoName: string;
</script>

{#if !$demoFilter || demoName.includes($demoFilter)}
  <div>
    <p>{demoName}</p>
  </div>
{/if}
