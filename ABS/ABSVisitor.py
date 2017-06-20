# Generated from ABS.g4 by ANTLR 4.7
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ABSParser.

class ABSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ABSParser#qualified_type_identifier.
    def visitQualified_type_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#qualified_identifier.
    def visitQualified_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#any_identifier.
    def visitAny_identifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#type_use.
    def visitType_use(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#type_exp.
    def visitType_exp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#paramlist.
    def visitParamlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#param_decl.
    def visitParam_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#interface_name.
    def visitInterface_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#delta_id.
    def visitDelta_id(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#EffExp.
    def visitEffExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#PureExp.
    def visitPureExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#GetExp.
    def visitGetExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#NewExp.
    def visitNewExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AsyncCallExp.
    def visitAsyncCallExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#SyncCallExp.
    def visitSyncCallExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#OriginalCallExp.
    def visitOriginalCallExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ConstructorExp.
    def visitConstructorExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FunctionExp.
    def visitFunctionExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AndExp.
    def visitAndExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#GreaterExp.
    def visitGreaterExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#MultExp.
    def visitMultExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#VarOrFieldExp.
    def visitVarOrFieldExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#StringExp.
    def visitStringExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#CaseExp.
    def visitCaseExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AddExp.
    def visitAddExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#NullExp.
    def visitNullExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#EqualExp.
    def visitEqualExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#VariadicFunctionExp.
    def visitVariadicFunctionExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IfExp.
    def visitIfExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#OrExp.
    def visitOrExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ParenExp.
    def visitParenExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#LetExp.
    def visitLetExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#UnaryExp.
    def visitUnaryExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IntExp.
    def visitIntExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ThisExp.
    def visitThisExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#casebranch.
    def visitCasebranch(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#UnderscorePattern.
    def visitUnderscorePattern(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IntPattern.
    def visitIntPattern(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#StringPattern.
    def visitStringPattern(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#VarPattern.
    def visitVarPattern(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ConstructorPattern.
    def visitConstructorPattern(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#var_or_field_ref.
    def visitVar_or_field_ref(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#pure_exp_list.
    def visitPure_exp_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#list_literal.
    def visitList_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#annotation.
    def visitAnnotation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#VardeclStmt.
    def visitVardeclStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AssignStmt.
    def visitAssignStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#SkipStmt.
    def visitSkipStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ReturnStmt.
    def visitReturnStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AssertStmt.
    def visitAssertStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#BlockStmt.
    def visitBlockStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IfStmt.
    def visitIfStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#WhileStmt.
    def visitWhileStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#TryCatchFinallyStmt.
    def visitTryCatchFinallyStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AwaitStmt.
    def visitAwaitStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#SuspendStmt.
    def visitSuspendStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DurationStmt.
    def visitDurationStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ThrowStmt.
    def visitThrowStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DieStmt.
    def visitDieStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#MoveCogToStmt.
    def visitMoveCogToStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ExpStmt.
    def visitExpStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#CaseStmt.
    def visitCaseStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ExpGuard.
    def visitExpGuard(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AndGuard.
    def visitAndGuard(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ClaimGuard.
    def visitClaimGuard(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DurationGuard.
    def visitDurationGuard(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#casestmtbranch.
    def visitCasestmtbranch(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#datatype_decl.
    def visitDatatype_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#data_constructor.
    def visitData_constructor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#data_constructor_arg.
    def visitData_constructor_arg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#typesyn_decl.
    def visitTypesyn_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#exception_decl.
    def visitException_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#function_decl.
    def visitFunction_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#interface_decl.
    def visitInterface_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#methodsig.
    def visitMethodsig(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#class_decl.
    def visitClass_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#field_decl.
    def visitField_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#method.
    def visitMethod(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#module_decl.
    def visitModule_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#module_export.
    def visitModule_export(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#module_import.
    def visitModule_import(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#decl.
    def visitDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#delta_decl.
    def visitDelta_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaFieldParam.
    def visitDeltaFieldParam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaClassParam.
    def visitDeltaClassParam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaHasFieldCondition.
    def visitDeltaHasFieldCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaHasMethodCondition.
    def visitDeltaHasMethodCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaHasInterfaceCondition.
    def visitDeltaHasInterfaceCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#delta_access.
    def visitDelta_access(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#module_modifier.
    def visitModule_modifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddFunctionModifier.
    def visitDeltaAddFunctionModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddDataTypeModifier.
    def visitDeltaAddDataTypeModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddTypeSynModifier.
    def visitDeltaAddTypeSynModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyTypeSynModifier.
    def visitDeltaModifyTypeSynModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyDataTypeModifier.
    def visitDeltaModifyDataTypeModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddClassModifier.
    def visitDeltaAddClassModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveClassModifier.
    def visitDeltaRemoveClassModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyClassModifier.
    def visitDeltaModifyClassModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddInterfaceModifier.
    def visitDeltaAddInterfaceModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveInterfaceModifier.
    def visitDeltaRemoveInterfaceModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyInterfaceModifier.
    def visitDeltaModifyInterfaceModifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddFieldFragment.
    def visitDeltaAddFieldFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveFieldFragment.
    def visitDeltaRemoveFieldFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddMethodFragment.
    def visitDeltaAddMethodFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaModifyMethodFragment.
    def visitDeltaModifyMethodFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveMethodFragment.
    def visitDeltaRemoveMethodFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddMethodsigFragment.
    def visitDeltaAddMethodsigFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaRemoveMethodsigFragment.
    def visitDeltaRemoveMethodsigFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddModuleImportFragment.
    def visitDeltaAddModuleImportFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#DeltaAddModuleExportFragment.
    def visitDeltaAddModuleExportFragment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#UpdateDecl.
    def visitUpdateDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ObjectUpdateDecl.
    def visitObjectUpdateDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ObjectUpdateAssignStmt.
    def visitObjectUpdateAssignStmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#UpdatePreambleDecl.
    def visitUpdatePreambleDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#productline_decl.
    def visitProductline_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#feature.
    def visitFeature(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#delta_clause.
    def visitDelta_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#deltaspec.
    def visitDeltaspec(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FIDAIDDeltaspecParam.
    def visitFIDAIDDeltaspecParam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#IntDeltaspecParam.
    def visitIntDeltaspecParam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#BoolOrIDDeltaspecParam.
    def visitBoolOrIDDeltaspecParam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#after_condition.
    def visitAfter_condition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#from_condition.
    def visitFrom_condition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#when_condition.
    def visitWhen_condition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureApplicationCondition.
    def visitFeatureApplicationCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#AndApplicationCondition.
    def visitAndApplicationCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#ParenApplicationCondition.
    def visitParenApplicationCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#NotApplicationCondition.
    def visitNotApplicationCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#OrApplicationCondition.
    def visitOrApplicationCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#attr_assignment.
    def visitAttr_assignment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#product_decl.
    def visitProduct_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#product_reconfiguration.
    def visitProduct_reconfiguration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#fextension.
    def visitFextension(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#feature_decl.
    def visitFeature_decl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#feature_decl_group.
    def visitFeature_decl_group(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#fnode.
    def visitFnode(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#feature_decl_attribute.
    def visitFeature_decl_attribute(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureDeclConstraintIfIn.
    def visitFeatureDeclConstraintIfIn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureDeclConstraintIfOut.
    def visitFeatureDeclConstraintIfOut(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureDeclConstraintExclude.
    def visitFeatureDeclConstraintExclude(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#FeatureDeclConstraintRequire.
    def visitFeatureDeclConstraintRequire(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#mexp.
    def visitMexp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#boundary_int.
    def visitBoundary_int(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#boundary_val.
    def visitBoundary_val(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#main_block.
    def visitMain_block(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#compilation_unit.
    def visitCompilation_unit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ABSParser#goal.
    def visitGoal(self, ctx):
        return self.visitChildren(ctx)


