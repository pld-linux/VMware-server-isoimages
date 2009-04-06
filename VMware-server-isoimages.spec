%define		ver	2.0.0
%define		subver	116503
Summary:	VMware Server - ISO images
Summary(pl.UTF-8):	Obrazy ISO dla VMware Servera
Name:		VMware-server-isoimages
Version:	%{ver}.%{subver}
Release:	1
License:	custom, non-distributable
Group:		Applications/Emulators
# http://www.vmware.com/download/server/
Source0:	http://download2.vmware.com/software/server/VMware-server-%{ver}-%{subver}.i386.tar.gz
# NoSource0-md5:	
NoSource:	0
URL:		http://www.vmware.com/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/lib
%define		imagedir	%{_libdir}/vmware/isoimages

%description
VMware Server Virtual Platform is a thin software layer that allows
multiple guest operating systems to run concurrently on a single
standard PC, without repartitioning or rebooting, and without
significant loss of performance.

This package contains ISO Images.

%description -l pl.UTF-8
VMware Server Virtual Platform to cienka warstwa oprogramowania
pozwalająca na jednoczesne działanie wielu gościnnych systemów
operacyjnych na jednym zwykłym PC, bez repartycjonowania ani
rebootowania, bez znacznej utraty wydajności.

Ten pakiet zawiera obrazy ISO.

%prep
%setup -qcT
%{__tar} -zxf %{SOURCE0} vmware-server-distrib/lib/isoimages

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{imagedir}
cp -a vmware-server-distrib/lib/isoimages/* $RPM_BUILD_ROOT%{imagedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{imagedir}
