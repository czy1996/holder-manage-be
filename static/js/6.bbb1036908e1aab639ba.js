webpackJsonp([6],{1045:function(e,t){e.exports={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"table"},[a("div",{staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-menu"}),e._v(" 书目管理")]),e._v(" "),a("el-breadcrumb-item",[e._v("书目")])],1)],1),e._v(" "),a("div",{staticClass:"handle-box"},[a("el-input",{staticClass:"handle-input mr10",attrs:{placeholder:"筛选关键词"},model:{value:e.select_word,callback:function(t){e.select_word=t},expression:"select_word"}}),e._v(" "),a("el-button",{attrs:{type:"primary",icon:"search"},on:{click:e.search}},[e._v("搜索")]),e._v(" "),a("el-button",{attrs:{type:"primary",icon:"plus"},on:{click:e.addBook}},[e._v("添加")])],1),e._v(" "),a("p",{staticStyle:{"font-size":"12px","line-height":"30px",color:"#999"}},[e._v("Tips : 单击行启用编辑，完成保存。")]),e._v(" "),a("el-table",{ref:"multipleTable",staticStyle:{width:"100%"},attrs:{data:e.data,border:"","highlight-current-row":""},on:{"selection-change":e.handleSelectionChange,"row-click":e.handleRowClick}},[a("el-table-column",{attrs:{type:"selection",width:"55"}}),e._v(" "),a("el-table-column",{attrs:{prop:"isbn",label:"ISBN",sortable:"",width:"150"}}),e._v(" "),a("el-table-column",{attrs:{prop:"title",label:"书名",width:"120"}}),e._v(" "),a("el-table-column",{attrs:{label:"定价"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-input",{directives:[{name:"show",rawName:"v-show",value:t.row.isEditFlag,expression:"scope.row.isEditFlag"}],attrs:{size:"small",placeholder:"请输入内容"},model:{value:t.row.second_price,callback:function(a){e.$set(t.row,"second_price",a)},expression:"scope.row.second_price"}}),e._v(" "),a("span",{directives:[{name:"show",rawName:"v-show",value:!t.row.isEditFlag,expression:"!scope.row.isEditFlag"}]},[e._v(e._s(t.row.second_price))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"库存"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-input",{directives:[{name:"show",rawName:"v-show",value:t.row.isEditFlag,expression:"scope.row.isEditFlag"}],attrs:{size:"small",placeholder:"请输入内容"},model:{value:t.row.inventory,callback:function(a){e.$set(t.row,"inventory",a)},expression:"scope.row.inventory"}}),e._v(" "),a("span",{directives:[{name:"show",rawName:"v-show",value:!t.row.isEditFlag,expression:"!scope.row.isEditFlag"}]},[e._v(e._s(t.row.inventory))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"180"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("el-button",{directives:[{name:"show",rawName:"v-show",value:t.row.isEditFlag,expression:"scope.row.isEditFlag"}],attrs:{size:"small"},on:{click:function(a){a.stopPropagation(),e.handleEditComplete(t.$index,t.row)}}},[e._v("完成\n                ")]),e._v(" "),a("el-button",{attrs:{size:"small",type:"danger"},on:{click:function(a){a.stopPropagation(),e.handleDelete(t.$index,t.row)}}},[e._v("删除\n                ")])]}}])})],1)],1)},staticRenderFns:[]}},1059:function(e,t,a){var i=a(676);"string"==typeof i&&(i=[[e.i,i,""]]),i.locals&&(e.exports=i.locals);a(199)("3abd669d",i,!0)},529:function(e,t,a){a(1059);var i=a(200)(a(574),a(1045),"data-v-2a005868",null);e.exports=i.exports},574:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default={data:function(){return{url:"./static/vuetable.json",tableData:[],cur_page:1,multipleSelection:[],select_cate:"",select_word:"",del_list:[],is_search:!1}},created:function(){this.getData()},computed:{data:function(){var e=this;return e.tableData.filter(function(t){for(var a=!1,i=0;i<e.del_list.length;i++)if(t.name===e.del_list[i].name){a=!0;break}if(!a&&(t.title.indexOf(e.select_word)>-1||t.description.indexOf(e.select_word)>-1))return e.$set(t,"isEditFlag",!1),t})}},methods:{handleCurrentChange:function(e){this.cur_page=e,this.getData()},getData:function(){var e=this;e.$book.all(function(t){e.tableData=t})},search:function(){this.is_search=!0},formatter:function(e,t){return e.address},filterTag:function(e,t){return t.tag===e},handleEditComplete:function(e,t){var a=this;this.$message("编辑第"+(e+1)+"行"),this.$book.update(t.id,{inventory:t.inventory,second_price:t.second_price},function(e){a.log(e)}),this.$set(t,"isEditFlag",!1)},handleDelete:function(e,t){this.$message.error("删除第"+(e+1)+"行")},delAll:function(){var e=this,t=e.multipleSelection.length,a="";e.del_list=e.del_list.concat(e.multipleSelection);for(var i=0;i<t;i++)a+=e.multipleSelection[i].name+" ";e.$message.error("删除了"+a),e.multipleSelection=[]},handleSelectionChange:function(e){this.multipleSelection=e},handleRowClick:function(e,t,a){this.log(e,t,a,e.isEditFlag),this.$set(e,"isEditFlag",!0),this.log(this.tableData)}}}},676:function(e,t,a){t=e.exports=a(88)(void 0),t.push([e.i,".handle-box[data-v-2a005868]{margin-bottom:20px}.handle-select[data-v-2a005868]{width:120px}.handle-input[data-v-2a005868]{width:300px;display:inline-block}",""])}});