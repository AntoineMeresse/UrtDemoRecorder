<script lang="ts">
  import { readDir, type FileEntry } from "@tauri-apps/api/fs";
  import { urtPath, getDemosFolder, demoList } from "$lib/urtService";
  import { onMount } from "svelte";
  import Demo from "./Demo.svelte";

  let errorMessage = "";

  function isDemo(elem: FileEntry) {
    return (
      !elem.children &&
      (elem.name?.includes(".dm_68") || elem.name?.includes(".urtdemo"))
    );
  }

  function loadDemosFiles() {
    if ($urtPath) {
      readDir(getDemosFolder($urtPath))
        .then((elems) => {
          let res: string[] = [];
          for (const e of elems) {
            if (isDemo(e) && e.name) {
              res.push(e.name);
            }
          }
          demoList.set(res);
        })
        .catch((error) => (errorMessage = error));
    }
  }

  onMount(() => {
    loadDemosFiles();
  });
</script>

<div>
  {#each $demoList as demo}
    <Demo demoName={demo} />
  {/each}
</div>
<p>{errorMessage}</p>
