%include	/usr/lib/rpm/macros.gstreamer

%define		gst_major_ver	1.0
%define		gst_req_ver	1.0
%define		gstpb_req_ver	1.0

Summary:	GStreamer extension library for non-linear editing
Name:		gstreamer-gnonlin
Version:	1.4.0
Release:	1
License:	LGPL
Group:		Applications/Multimedia
Source0:	http://gstreamer.freedesktop.org/src/gnonlin/gnonlin-%{version}.tar.xz
# Source0-md5:	106899d1ee36e18f92bb838244d585eb
URL:		http://gnonlin.sourceforge.net/
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	rpm-gstreamerprov
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnonlin is a plugin for GStreamer which provides support for writing
non-linear audio and video editing applications. It introduces the
concept of a timeline.

%prep
%setup -qn gnonlin-%{version}

%build
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgnl.so

