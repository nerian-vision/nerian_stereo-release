Name:           ros-melodic-nerian-stereo
Version:        3.0.2
Release:        0%{?dist}
Summary:        ROS nerian_stereo package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/nerian_stereo
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       boost-devel
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs

%description
Driver node for SceneScan and SP1 stereo vision sensors by Nerian Vision
Technologies

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Aug 08 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.0.2-0
- Autogenerated by Bloom

* Mon Aug 06 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.0.1-0
- Autogenerated by Bloom

* Fri Jun 08 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.0.0-0
- Autogenerated by Bloom

* Sun May 13 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 2.2.0-0
- Autogenerated by Bloom

