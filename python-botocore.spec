%global debug_package %{nil}

Name: python-botocore
Epoch: 100
Version: 1.27.47
Release: 1%{?dist}
BuildArch: noarch
Summary: Low-level, data-driven core of boto 3
License: Apache-2.0
URL: https://github.com/boto/botocore/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-botocore
Summary: Low-level, data-driven core of boto 3
Requires: python3
Requires: python3-python-dateutil >= 2.1
Requires: python3-jmespath >= 0.7.1
Requires: python3-urllib3 >= 1.25.4
Provides: python3-botocore = %{epoch}:%{version}-%{release}
Provides: python3dist(botocore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-botocore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(botocore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-botocore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(botocore) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-botocore
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%files -n python%{python3_version_nodots}-botocore
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-botocore
Summary: Low-level, data-driven core of boto 3
Requires: python3
Requires: python3-python-dateutil >= 2.1
Requires: python3-jmespath >= 0.7.1
Requires: python3-urllib3 >= 1.25.4
Provides: python3-botocore = %{epoch}:%{version}-%{release}
Provides: python3dist(botocore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-botocore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(botocore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-botocore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(botocore) = %{epoch}:%{version}-%{release}

%description -n python3-botocore
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%files -n python3-botocore
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if 0%{?centos_version} == 700
%package -n python%{python3_version_nodots}-botocore
Summary: Low-level, data-driven core of boto 3
Requires: python3
Requires: python36-dateutil >= 2.1
Requires: python3-jmespath >= 0.7.1
Requires: python3-urllib3 >= 1.25.4
Provides: python3-botocore = %{epoch}:%{version}-%{release}
Provides: python3dist(botocore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-botocore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(botocore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-botocore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(botocore) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-botocore
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%files -n python%{python3_version_nodots}-botocore
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?centos_version} == 700)
%package -n python3-botocore
Summary: Low-level, data-driven core of boto 3
Requires: python3
Requires: python3-dateutil >= 2.1
Requires: python3-jmespath >= 0.7.1
Requires: python3-urllib3 >= 1.25.4
Provides: python3-botocore = %{epoch}:%{version}-%{release}
Provides: python3dist(botocore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-botocore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(botocore) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-botocore = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(botocore) = %{epoch}:%{version}-%{release}

%description -n python3-botocore
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%files -n python3-botocore
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
