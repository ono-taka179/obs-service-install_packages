# obs-service-install_packages
obs-service-install_packages is a source service for OpenSUSE Build Service. This service installs multiple packages with the same name for different architectures in the build environment. This is composed of the following files.
# How to use
## Prepare packages for installation
Prepare the packages you want to install and place it in the `obs-service-install_packages-0.1.0` directory (Please remove hoge.rpm). This service only supports RPM installation via dnf, so if you want to use other formats, script modifications are necessary.
## install_packages script
`obs-service-install_packages-0.1.0/install_packages` 
## SPEC

## Building obs-service-install_packages

## _service
