Name:           ros-kinetic-nerian-stereo
Version:        2.2.0
Release:        1%{?dist}
Summary:        ROS nerian_stereo package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/nerian_stereo
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       boost-devel
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs

%description
Driver node for SceneScan and SP1 stereo vision sensors by Nerian Vision
Technologies

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun May 13 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 2.2.0-1
- Autogenerated by Bloom

* Sun May 13 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 2.2.0-0
- Autogenerated by Bloom

* Sat Dec 09 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 2.1.0-0
- Autogenerated by Bloom

* Fri Oct 20 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 2.0.3-0
- Autogenerated by Bloom

* Wed Oct 18 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 2.0.2-0
- Autogenerated by Bloom

* Wed Oct 04 2017 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 2.0.1-0
- Autogenerated by Bloom

