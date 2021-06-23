Name:		partclone
Version:	0.3.17
Release:	1
Group:		System/Configuration/Other
URL:		http://partclone.sf.net
License:	GPLv2
Summary:	File System Clone Utilities
Source0:	https://sourceforge.net/projects/partclone/files/source/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ext2fs)
BuildRequires:	pkgconfig(libntfs-3g)
BuildRequires:	ncursesw-devel
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libbsd)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	btrfs-devel
BuildRequires:	nilfs-utils-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(fuse)

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
%autosetup -p1

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
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_datadir}/partclone/fail-mbr.bin

