import { writable, type Writable, get } from "svelte/store";
import { readDir, type FileEntry } from "@tauri-apps/api/fs";
import { DemoFormats } from "./demos/DemoFormats";

export const urtPath : Writable<string> = writable("");
export const demoList : Writable<string[]> = writable([]);
export const demoNameFilter : Writable<string> = writable("")
export const demoTypeFilter : Writable<string> = writable(DemoFormats[0])

export function removeExecFromPath(execpath : string) : string{
    const pathSplit = execpath.split('\\');
    const path = pathSplit.slice(0,-1).join('\\')
    console.log(path);
    return path;
}

function isDemo(elem: FileEntry) : boolean{
    const isFile : boolean = elem.children === undefined;
    const demoType = get(demoTypeFilter);
    let hasDemoExtension : boolean;
    if (demoType === DemoFormats[0]) {
        hasDemoExtension = (elem.name?.includes(".dm_68") || elem.name?.includes(".urtdemo")) ? true : false;
    } else {
        hasDemoExtension = elem.name?.includes(demoType) ? true : false;
    }
    
    return isFile && hasDemoExtension;
  }

export function loadDemosFiles() : void {
    const path = get(urtPath);
    if (path) {
      readDir(getDemosFolder(path))
        .then((elems) => {
          let res: string[] = [];
          for (const e of elems) {
            if (isDemo(e) && e.name) {
              res.push(e.name);
            }
          }
          demoList.set(res);
        })
    }
  }


export function getDemosFolder(urtPath : string) : string {
    return removeExecFromPath(urtPath) + "\\q3ut4\\demos"; // Only works for windows users
}