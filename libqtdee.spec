%define major 2
%define libname %mklibname qtdee  %{major}
%define develname %mklibname qtdee -d

Name:		libqtdee
Version:	0.2.3
Release:	1
License:	GPLv3
Summary:	Qt bindings and QML plugin for Dee
Url:		http://launchat.net/dee-qt
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE - libqtdee-cmake-libdir-fix.patch nmarques@opensuse.org -- this is becoming epic.
Patch0:		libqtdee-cmake-libdir-fix.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(dee-1.0)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtDeclarative)

%description
Qt binding and QML plugin for Dee.
Simple Qt binding and QML plugin for Dee (https://launchpad.net/dee).

%package -n %{libname}
Summary:	Qt bindings and QML plugin for Dee - shared libraries
Group:		System/Libraries

%description -n %{libname}
Qt binding and QML plugin for Dee - system shared libraries.
Simple Qt binding and QML plugin for Dee (https://launchpad.net/dee).

%package -n %{develname}
Summary:	Qt bindings and QML plugin for Dee - development files
Group:		Development/C++
Requires:	%{libname} = %{version}

%description -n %{develname}
t binding and QML plugin for Dee - development files.
Simple Qt binding and QML plugin for Dee (https://launchpad.net/dee).

%prep
%setup -q
%apply_patches

%build
export BUILD_GLOBAL=true
%cmake \
	-Dlibdir=%{_libdir} \

%make

%install
pushd build
# .pc file hack
sed -i 's/libdir=\${exec_prefix}\/lib/libdir=\${exec_prefix}\/%{_lib}/g' ../libqtdee.pc
%makeinstall_std
popd

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.%{major}*
%{_libdir}/qt4/plugins/imports/

%files -n %{develname}
%{_includedir}/QtDee/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libqtdee.pc

