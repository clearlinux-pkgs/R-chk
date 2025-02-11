#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : R-chk
Version  : 0.10.0
Release  : 10
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/chk_0.10.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/chk_0.10.0.tar.gz
Summary  : Check User-Supplied Function Arguments
Group    : Development/Tools
License  : MIT
Requires: R-lifecycle
Requires: R-rlang
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
is designed to be simple, fast and customizable.  Error messages
    follow the tidyverse style guide.

%prep
%setup -q -n chk
pushd ..
cp -a chk buildavx2
popd
pushd ..
cp -a chk buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737997824

%install
export SOURCE_DATE_EPOCH=1737997824
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/chk/DESCRIPTION
/usr/lib64/R/library/chk/INDEX
/usr/lib64/R/library/chk/LICENSE
/usr/lib64/R/library/chk/Meta/Rd.rds
/usr/lib64/R/library/chk/Meta/features.rds
/usr/lib64/R/library/chk/Meta/hsearch.rds
/usr/lib64/R/library/chk/Meta/links.rds
/usr/lib64/R/library/chk/Meta/nsInfo.rds
/usr/lib64/R/library/chk/Meta/package.rds
/usr/lib64/R/library/chk/Meta/vignette.rds
/usr/lib64/R/library/chk/NAMESPACE
/usr/lib64/R/library/chk/NEWS.md
/usr/lib64/R/library/chk/R/chk
/usr/lib64/R/library/chk/R/chk.rdb
/usr/lib64/R/library/chk/R/chk.rdx
/usr/lib64/R/library/chk/WORDLIST
/usr/lib64/R/library/chk/doc/chk-families.R
/usr/lib64/R/library/chk/doc/chk-families.Rmd
/usr/lib64/R/library/chk/doc/chk-families.html
/usr/lib64/R/library/chk/doc/chk.R
/usr/lib64/R/library/chk/doc/chk.Rmd
/usr/lib64/R/library/chk/doc/chk.html
/usr/lib64/R/library/chk/doc/index.html
/usr/lib64/R/library/chk/help/AnIndex
/usr/lib64/R/library/chk/help/aliases.rds
/usr/lib64/R/library/chk/help/chk.rdb
/usr/lib64/R/library/chk/help/chk.rdx
/usr/lib64/R/library/chk/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/chk/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/chk/help/figures/logo.png
/usr/lib64/R/library/chk/help/paths.rds
/usr/lib64/R/library/chk/html/00Index.html
/usr/lib64/R/library/chk/html/R.css
/usr/lib64/R/library/chk/tests/testthat.R
/usr/lib64/R/library/chk/tests/testthat/test-aaa-deprecated.R
/usr/lib64/R/library/chk/tests/testthat/test-cc.R
/usr/lib64/R/library/chk/tests/testthat/test-check-data.R
/usr/lib64/R/library/chk/tests/testthat/test-check-dim.R
/usr/lib64/R/library/chk/tests/testthat/test-check-dirs.R
/usr/lib64/R/library/chk/tests/testthat/test-check-files.R
/usr/lib64/R/library/chk/tests/testthat/test-check-key.R
/usr/lib64/R/library/chk/tests/testthat/test-check-length.R
/usr/lib64/R/library/chk/tests/testthat/test-check-names.R
/usr/lib64/R/library/chk/tests/testthat/test-check-values.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-all.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-array.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-atomic.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-character-or-factor.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-character.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-chr.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-compatible-lengths.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-complex-number.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-complex.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-count.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-data.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-date-time.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-date.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-dbl.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-double.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-environment.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-factor.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-file.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-identical.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-integer.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-is.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-join.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-length.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-lgl.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-logical.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-matrix.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-missing.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-not-any-na.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-not-empty.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-not-missing.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-not-subset.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-null-or.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-null.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-number.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-numeric.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-orderset.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-range.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-raw.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-setequal.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-sorted.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-string.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-subset.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-superset.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-true.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-type.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-tz.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-unique.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-unused.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-valid-name.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-vector.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-whole-number.R
/usr/lib64/R/library/chk/tests/testthat/test-chk-wnum.R
/usr/lib64/R/library/chk/tests/testthat/test-chkor-vld.R
/usr/lib64/R/library/chk/tests/testthat/test-chkor.R
/usr/lib64/R/library/chk/tests/testthat/test-err.R
/usr/lib64/R/library/chk/tests/testthat/test-expect-chk-error.R
/usr/lib64/R/library/chk/tests/testthat/test-internal.R
/usr/lib64/R/library/chk/tests/testthat/test-p.R
/usr/lib64/R/library/chk/tests/testthat/test-utils.R
