Installing SphinxSE
-------------------

You will need to obtain a copy of MySQL sources, prepare those, and then
recompile MySQL binary. MySQL sources (mysql-5.x.yy.tar.gz) could be
obtained from `dev.mysql.com <http://dev.mysql.com>`__ Web site.

For some MySQL versions, there are delta tarballs with already prepared
source versions available from Sphinx Web site. After unzipping those
over original sources MySQL would be ready to be configured and built
with Sphinx support.

If such tarball is not available, or does not work for you for any
reason, you would have to prepare sources manually. You will need to GNU
Autotools framework (autoconf, automake and libtool) installed to do
that.
