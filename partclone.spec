%define release %mkrel 1

Name:         partclone
Version:      0.0.6	 
Release:      %{release}
Group:        System/Configuration/Other
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

%changelog
* Thu Feb 21 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.6-3
- Bug fixed: clone.fat was not compiled.

* Thu Feb 21 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.6-1
- New upstream 0.0.6-1.

* Sat Feb 16 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.5-16
- New upstream 0.0.5-16.

* Mon Feb 04 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.5-15
- New upstream 0.0.5-15.

* Thu Jan 24 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.5-10
- New upstream 0.0.5-10.

* Fri Jan 04 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.5-1
- New upstream 0.0.5-1.

* Thu Jan 03 2008 - Steven Shiau <steven _at_ nchc org tw> 0.0.4-4
- Sync the version number with Debian package.
- Enable static linking.

* Mon Dec 31 2007 - Steven Shiau <steven _at_ nchc org tw> 0.0.1-2
- Some doc and debian rules were added by Thomas Tsai.

* Mon Dec 10 2007 - Steven Shiau <steven _at_ nchc org tw> 0.0.1-1
- Initial release for partclone.
