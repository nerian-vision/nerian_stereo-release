Name:           ros-melodic-nerian-stereo
Version:        3.5.0
Release:        1%{?dist}
Summary:        ROS nerian_stereo package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/nerian_stereo
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python2-devel
Requires:       boost-python3-devel
Requires:       curl
Requires:       libcurl-devel
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nodelet
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
BuildRequires:  boost-devel
BuildRequires:  boost-python2-devel
BuildRequires:  boost-python3-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs

%description
Driver node for SceneScan and SP1 stereo vision sensors by Nerian Vision GmbH

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
* Thu Aug 15 2019 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.5.0-1
- Autogenerated by Bloom

* Wed Jun 19 2019 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.4.0-1
- Autogenerated by Bloom

* Fri Feb 15 2019 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.3.2-0
- Autogenerated by Bloom

* Fri Feb 08 2019 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.3.1-0
- Autogenerated by Bloom

* Mon Feb 04 2019 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.3.0-1
- Autogenerated by Bloom

* Mon Feb 04 2019 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.3.0-0
- Autogenerated by Bloom

* Mon Feb 04 2019 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.2.1-1
- Autogenerated by Bloom

* Wed Dec 05 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.2.1-0
- Autogenerated by Bloom

* Tue Nov 27 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.2.0-0
- Autogenerated by Bloom

* Tue Nov 13 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.1.1-0
- Autogenerated by Bloom

* Sat Nov 10 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.1.0-0
- Autogenerated by Bloom

* Wed Aug 08 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.0.2-0
- Autogenerated by Bloom

* Mon Aug 06 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.0.1-0
- Autogenerated by Bloom

* Fri Jun 08 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 3.0.0-0
- Autogenerated by Bloom

* Sun May 13 2018 Konstantin Schauwecker <konstantin.schauwecker@nerian.com> - 2.2.0-0
- Autogenerated by Bloom

