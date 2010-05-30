<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="default.aspx.cs" Inherits="KingOfKmaps._default" %>
<%@ Register TagPrefix="kmaps" TagName="Grid" Src="~/grid.ascx"  %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>King Of Kmaps</title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <kmaps:Grid runat="server"></kmaps:Grid>
    </div>
    </form>
</body>
</html>
