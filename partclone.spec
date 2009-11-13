%define release %mkrel 1

Name:         partclone
Version:      0.1.9
Release:      %{release}
Group:        System/Configuration/Other
URL:          http://partclone.sf.net
License:      GPL2
Summary:      File System Clone Utilities
Source0:      %{name}_%{version}-3.tar.gz
Patch0:		  configure.patch
Patch1:		  libxfs.patch
BuildRequires: e2fsprogs-devel
BuildRequires: reiser4progs
BuildRequires: xfsprogs-devel
BuildRequires: libntfs-devel
BuildRequires: xfs-devel
#BuildRequires: reiser4progs-devel
BuildRoot:    %{_tmppath}/%{name}-build

%description
A set of file system clone utilities, including
ext2/3, reiserfs, reiser4, xfs, hfs+ file system.

Authors:
--------
    Thomas Tsai <Thomas _at_ nchc org tw>
    Jazz Wang <jazz _at_ nchc org tw>
    http://partclone.sourceforge.net 
    http://partclone.nchc.org.tw

%prep
%setup -q 
%patch0
%patch1

%build
autoconf
%configure --enable-ntfs --enable-extfs --enable-hfsp --enable-fat
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*
%lang(zh) /usr/share/locale/zh_TW/LC_MESSAGES/partclone.mo
