Name:		partclone
Version:	0.3.13
Release:	1
Group:		System/Configuration/Other
URL:		http://partclone.sf.net
License:	GPLv2
Summary:	File System Clone Utilities
Source0:	https://sourceforge.net/projects/partclone/files/source/%{name}-%{version}.tar.gz
BuildRequires:	ext2fs-devel
BuildRequires:	pkgconfig(libntfs-3g)
BuildRequires:	ncursesw-devel
BuildRequires:	ncurses-devel
BuildRequires:	libuuid-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  btrfs-devel
BuildRequires:	nilfs-utils-devel
BuildRequires:	gettext-devel
BuildRequires:  pkgconfig(fuse)



%description
Partclone provides utilities to back up and restore used-blocks of a partition
and it is designed for higher compatibility of the file system by using
existing library, e.g. e2fslibs is used to read and write the ext2 partition.

Authors:
--------
    Thomas Tsai <Thomas _at_ nchc org tw>
    Jazz Wang <jazz _at_ nchc org tw>
    http://partclone.sourceforge.net 
    http://partclone.nchc.org.tw

%prep
%setup -q 

%build
%configure \
	--enable-extfs \
	--enable-hfsp \
	--enable-fat \
	--enable-ntfs \
	--enable-btrfs \
	--enable-ncursesw \
	--enable-fs-test \
	--enable-xfs \
	--enable-exfat \
	--enable-f2fs \
	--enable-nilfs2 \
	--enable-minix
%make_build

%install
%make_install
%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_datadir}/partclone/fail-mbr.bin


%changelog
* Fri Jun 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.48-1mdv2011.0
+ Revision: 801781
- update to 0.2.48

* Mon Dec 19 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.38-1
+ Revision: 743700
- BR ncurses-devel added
- added BR libuuid-devel, smp build re-enabled
- disable smp build
- autoconf not needed
- update to 0.2.38

  + Jerome Martin <jmartin@mandriva.org>
    - Updated to 0.1.9

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Leonardo de Amaral Vidal <leonardoav@mandriva.com>
    - Spec package fix

* Mon Jul 07 2008 Leonardo de Amaral Vidal <leonardoav@mandriva.com> 0.0.6-1mdv2009.0
+ Revision: 232459
- partclone package built
- import partclone


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
