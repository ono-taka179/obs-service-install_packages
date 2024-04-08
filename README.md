# obs-service-install_packages

obs-service-install_packages is a source service for OpenSUSE Build Service. This service installs multiple packages with the same name for different architectures in the build environment. This is composed of the following files.

# How to use

## Prepare packages for installation

Prepare the packages you want to install and place it in the `obs-service-install_packages-0.1.0` directory (hoge.rpm is dummy, please remove it). These packages are installed by installing obs-service-install_packages. This service only supports RPM installation via dnf, so if you want to use other formats, modifying script is necessary.

## install_packages script

`obs-service-install_packages-0.1.0/install_packages` executes the following actions: 

- Check if the package assigned to `CHECKINSTALLED` is installed
- Install the packages included in obs-service-install_packages

The packages are located in `SERVICEDIR` , but if necessary, it can be modified in the spec.

## Create tar.gz

Create a tar.gz file with a name corresponding to the value of `Source:` in the spec.

```
tar czvf obs-service-install_packages-0.1.0.tar.gz /path/to/obs-service-install_packages-0.1.0
```

## SPEC

The installation destination for the packages placed in `obs-service-install_packages-0.1.0` is specified as `/usr/lib/obs/service` in the build environment.

## Building obs-service-install_packages

There are various methods for this. You can register tar.gz file and spec file in the OBS repository and build them. Alternatively, you can create RPM using rpmbuild and import them into OBS. Both methods use the package name `obs-service-install_packages` .

## _service

To execute the service during build, specify `mode` as `buildtime` . By specifying `name` as `install_packages` , it is equivalent to specifying `obs-service-install_packages` in `BuildRequires` . Add `_service` to the repository of the package you want to use this service.
