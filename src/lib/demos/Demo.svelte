<script lang="ts">
  import { demoNameFilter, demoListSelected } from "$lib/urtService";
  export let demoName: string;

  function isInSelectedList(): boolean {
    return $demoListSelected.includes(demoName);
  }

  function updateSelectedList() {
    let demoListSelectedCpy = [...$demoListSelected];
    console.log(demoListSelectedCpy);
    if (!isInSelectedList()) {
      demoListSelected.set([...demoListSelectedCpy, demoName]);
    } else {
      demoListSelected.set(demoListSelectedCpy.filter((e) => e !== demoName));
    }
  }
</script>

{#if !$demoNameFilter || demoName.includes($demoNameFilter)}
  <div>
    <input
      type="checkbox"
      on:click={updateSelectedList}
      checked={isInSelectedList()}
    />
    <span>{demoName}</span>
  </div>
{/if}

<style>
  div {
    display: flex;
    justify-content: start;
    margin-top: 2vh;
  }
</style>
