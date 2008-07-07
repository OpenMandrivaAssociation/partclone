%define release %mkrel 1

Name:         partclone
Version:      0.0.6	 
Release:      %{release}
Group:        System/Filesystems
URL:          http://partclone.sf.net
License:      GPL
Summary:      File System Clone Utilities for ext2/3, reiserfs, reiser4, xfs, hfs+ File System
Source0:      %{name}_%{version}-3.tar.gz
BuildRequires: e2fsprogs-devel, reiser4progs, xfsprogs-devel, 
BuildRoot:    %{_tmppath}/%{name}-build

%description
A set of file system clone utilities, including
ext2/3, reiserfs, reiser4, xfs, hfs+ file system

Authors:
--------
    Thomas Tsai <Thomas _at_ nchc org tw>
    Jazz Wang <jazz _at_ nchc org tw>
    http://partclone.sourceforge.net, http://partclone.nchc.org.tw

%prep
%setup -q -n %{name}

%build
%configure
%make

%install
%makeinstall

%post

%postun
ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*
/usr/share/locale/*

