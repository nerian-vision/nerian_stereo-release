%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-nerian-stereo
Version:        3.9.0
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS nerian_stereo package

License:        MIT
URL:            http://wiki.ros.org/nerian_stereo
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       curl
Requires:       libcurl-devel
Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-stereo-msgs
Requires:       ros-noetic-tf2
Requires:       ros-noetic-tf2-ros
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-stereo-msgs
BuildRequires:  ros-noetic-tf2
BuildRequires:  ros-noetic-tf2-ros
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Driver node for Scarlet and SceneScan stereo vision sensors by Nerian Vision
GmbH

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Apr 14 2021 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.9.0-4
- Autogenerated by Bloom

* Wed Apr 14 2021 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.9.0-3
- Autogenerated by Bloom

* Wed Apr 14 2021 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.9.0-2
- Autogenerated by Bloom

* Wed Apr 14 2021 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.9.0-1
- Autogenerated by Bloom

* Thu Jul 30 2020 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.8.1-1
- Autogenerated by Bloom

* Wed Jul 29 2020 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.8.0-1
- Autogenerated by Bloom

* Wed Jul 29 2020 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.7.0-1
- Autogenerated by Bloom

