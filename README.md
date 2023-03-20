# depth_segmentation_maps

Calculated depth and segmentation maps for several models and additional analysis.

This repository is part of [Sohpappeal](https://github.com/Telecommunication-Telemedia-Assessment/sophoappeal).
Please use the main repository as starting point.

This repository is part of the DFG project [Sophoappeal (437543412)](https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-elektrotechnik-und-informationstechnik/profil/institute-und-fachgebiete/fachgebiet-audiovisuelle-technik/forschung/dfg-projekt-sophoappeal), it contains images and analysis scripts.

## Calculate maps
* requires ../images to be the [sohpappeal_images](https://github.com/Telecommunication-Telemedia-Assessment/sophoappeal_images) repository, it is recommended to use the main repository [Sohpappeal](https://github.com/Telecommunication-Telemedia-Assessment/sophoappeal).

* DPT implementation see: https://github.com/intel-isl/DPT
    * checkout DPT repo
    * install according to the given readme via conda
    * run `pip3 install python-dateutil` (dependency is missing) inside the newly created conda environment
    * place `dpt_do_all.py` in the folder, adapt paths inside this script
        * you may change "gpu" to "cpu" in the run_*.py scripts of DPT
    * `dpt_do_all.py` should generate in <DPT_Folder>/maps the same content as stored in the DPT subfolder in this repo



## Requirements

* python3, python3-pip, git, imagemagick, wget, unzip
* jupyternotebook for the analysis scripts

Run `./prepare.sh` to download the depth and segmentation maps.


## Structure and scripts


* `DPT/depths`: depths maps
* `DPT/segmentation`: segmentation maps

* `calc_depth.py`: calculates statistics of the depths maps
* `calc_segmentation.py`: calculates statistics of the segmentation maps
* `dpt_do_all.py`: script to rerun DPT



## Acknowledgments

If you use this software or data in your research, please include a link to the repository and reference the following paper.

```bibtex
@article{goering2023imageappeal,
  title={Image Appeal Revisited: Analysis, new Dataset and Prediction Models},
  author={Steve G\"oring and Alexander Raake},
  journal={IEEE Access},
  year={2023},
  publisher={IEEE},
  note={to appear}
}
```

## License
GNU General Public License v3. See [LICENSE.md](./LICENSE.md) file in this repository.
