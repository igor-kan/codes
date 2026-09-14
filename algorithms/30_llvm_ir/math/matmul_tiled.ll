; ModuleID = 'algorithms/02_c/math/matmul_tiled.c'
source_filename = "algorithms/02_c/math/matmul_tiled.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [29 x i8] c"C[i * N + j] == A[i * N + j]\00", align 1
@.str.1 = private unnamed_addr constant [36 x i8] c"algorithms/02_c/math/matmul_tiled.c\00", align 1
@__PRETTY_FUNCTION__.main = private unnamed_addr constant [15 x i8] c"int main(void)\00", align 1
@str = private unnamed_addr constant [66 x i8] c"[C Matrix] Tiled matrix multiplication verified against identity.\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @matmul_tiled(ptr noundef readonly captures(none) %0, ptr noundef readonly captures(none) %1, ptr noundef captures(none) %2, i32 noundef %3) local_unnamed_addr #0 {
  %5 = icmp sgt i32 %3, 0
  br i1 %5, label %6, label %77

6:                                                ; preds = %4
  %7 = zext nneg i32 %3 to i64
  %8 = shl nuw nsw i64 %7, 3
  %9 = and i64 %7, 3
  %10 = icmp ult i32 %3, 4
  br i1 %10, label %15, label %11

11:                                               ; preds = %6
  %12 = and i64 %7, 2147483644
  br label %37

13:                                               ; preds = %37
  %14 = icmp eq i64 %9, 0
  br i1 %14, label %29, label %15

15:                                               ; preds = %13, %6
  %16 = phi i64 [ 0, %6 ], [ %63, %13 ]
  %17 = icmp ne i64 %9, 0
  tail call void @llvm.assume(i1 %17)
  br label %18

18:                                               ; preds = %18, %15
  %19 = phi i64 [ %16, %15 ], [ %26, %18 ]
  %20 = phi i64 [ 0, %15 ], [ %27, %18 ]
  %21 = trunc nuw nsw i64 %19 to i32
  %22 = mul i32 %3, %21
  %23 = zext i32 %22 to i64
  %24 = shl nuw nsw i64 %23, 3
  %25 = getelementptr i8, ptr %2, i64 %24
  tail call void @llvm.memset.p0.i64(ptr align 8 %25, i8 0, i64 %8, i1 false), !tbaa !9
  %26 = add nuw nsw i64 %19, 1
  %27 = add i64 %20, 1
  %28 = icmp eq i64 %27, %9
  br i1 %28, label %29, label %18, !llvm.loop !11

29:                                               ; preds = %18, %13
  %30 = zext nneg i32 %3 to i64
  %31 = shl nuw nsw i64 %7, 7
  %32 = shl nuw nsw i64 %7, 3
  %33 = zext nneg i32 %3 to i64
  %34 = shl nuw nsw i64 %7, 7
  %35 = shl nuw nsw i64 %7, 3
  %36 = zext nneg i32 %3 to i64
  br label %66

37:                                               ; preds = %37, %11
  %38 = phi i64 [ 0, %11 ], [ %63, %37 ]
  %39 = phi i64 [ 0, %11 ], [ %64, %37 ]
  %40 = trunc nuw nsw i64 %38 to i32
  %41 = mul i32 %3, %40
  %42 = zext i32 %41 to i64
  %43 = shl nuw nsw i64 %42, 3
  %44 = getelementptr i8, ptr %2, i64 %43
  tail call void @llvm.memset.p0.i64(ptr align 8 %44, i8 0, i64 %8, i1 false), !tbaa !9
  %45 = trunc i64 %38 to i32
  %46 = or disjoint i32 %45, 1
  %47 = mul i32 %3, %46
  %48 = zext i32 %47 to i64
  %49 = shl nuw nsw i64 %48, 3
  %50 = getelementptr i8, ptr %2, i64 %49
  tail call void @llvm.memset.p0.i64(ptr align 8 %50, i8 0, i64 %8, i1 false), !tbaa !9
  %51 = trunc i64 %38 to i32
  %52 = or disjoint i32 %51, 2
  %53 = mul i32 %3, %52
  %54 = zext i32 %53 to i64
  %55 = shl nuw nsw i64 %54, 3
  %56 = getelementptr i8, ptr %2, i64 %55
  tail call void @llvm.memset.p0.i64(ptr align 8 %56, i8 0, i64 %8, i1 false), !tbaa !9
  %57 = trunc i64 %38 to i32
  %58 = or disjoint i32 %57, 3
  %59 = mul i32 %3, %58
  %60 = zext i32 %59 to i64
  %61 = shl nuw nsw i64 %60, 3
  %62 = getelementptr i8, ptr %2, i64 %61
  tail call void @llvm.memset.p0.i64(ptr align 8 %62, i8 0, i64 %8, i1 false), !tbaa !9
  %63 = add nuw nsw i64 %38, 4
  %64 = add i64 %39, 4
  %65 = icmp eq i64 %64, %12
  br i1 %65, label %13, label %37, !llvm.loop !13

66:                                               ; preds = %98, %29
  %67 = phi i64 [ %102, %98 ], [ 0, %29 ]
  %68 = phi i64 [ %99, %98 ], [ 0, %29 ]
  %69 = mul i64 %31, %67
  %70 = trunc i64 %68 to i32
  %71 = add nuw nsw i32 %70, 16
  %72 = tail call i32 @llvm.smin.i32(i32 %71, i32 %3)
  %73 = sext i32 %72 to i64
  %74 = getelementptr i8, ptr %2, i64 %69
  %75 = getelementptr i8, ptr %2, i64 %69
  %76 = getelementptr i8, ptr %75, i64 8
  br label %78

77:                                               ; preds = %98, %4
  ret void

78:                                               ; preds = %66, %136
  %79 = phi i64 [ 0, %66 ], [ %140, %136 ]
  %80 = phi i64 [ 0, %66 ], [ %137, %136 ]
  %81 = mul i64 %34, %79
  %82 = add nuw i64 %80, 16
  %83 = tail call i64 @llvm.smin.i64(i64 %82, i64 %33)
  %84 = or disjoint i64 %80, 1
  %85 = tail call i64 @llvm.smax.i64(i64 %83, i64 %84)
  %86 = shl i64 %79, 4
  %87 = xor i64 %86, -1
  %88 = add i64 %85, %87
  %89 = mul i64 %35, %88
  %90 = trunc i64 %80 to i32
  %91 = add nuw nsw i32 %90, 16
  %92 = tail call i32 @llvm.smin.i32(i32 %91, i32 %3)
  %93 = sext i32 %92 to i64
  %94 = getelementptr i8, ptr %1, i64 %81
  %95 = getelementptr i8, ptr %1, i64 %81
  %96 = getelementptr i8, ptr %95, i64 8
  %97 = getelementptr i8, ptr %96, i64 %89
  br label %103

98:                                               ; preds = %136
  %99 = add nuw nsw i64 %68, 16
  %100 = trunc i64 %99 to i32
  %101 = icmp sgt i32 %3, %100
  %102 = add i64 %67, 1
  br i1 %101, label %66, label %77, !llvm.loop !15

103:                                              ; preds = %153, %78
  %104 = phi i64 [ %157, %153 ], [ 0, %78 ]
  %105 = phi i64 [ %154, %153 ], [ 0, %78 ]
  %106 = add nuw i64 %105, 16
  %107 = tail call i64 @llvm.smin.i64(i64 %106, i64 %36)
  %108 = or disjoint i64 %105, 1
  %109 = tail call i64 @llvm.smax.i64(i64 %107, i64 %108)
  %110 = shl i64 %104, 4
  %111 = sub i64 %109, %110
  %112 = shl nuw nsw i64 %104, 7
  %113 = add nuw i64 %105, 16
  %114 = tail call i64 @llvm.smin.i64(i64 %113, i64 %33)
  %115 = or disjoint i64 %105, 1
  %116 = tail call i64 @llvm.smax.i64(i64 %114, i64 %115)
  %117 = shl i64 %104, 4
  %118 = xor i64 %117, -1
  %119 = add i64 %116, %118
  %120 = shl nsw i64 %119, 3
  %121 = getelementptr i8, ptr %94, i64 %112
  %122 = getelementptr i8, ptr %97, i64 %112
  %123 = getelementptr i8, ptr %122, i64 %120
  %124 = trunc i64 %105 to i32
  %125 = add nuw nsw i32 %124, 16
  %126 = tail call i32 @llvm.smin.i32(i32 %125, i32 %3)
  %127 = sext i32 %126 to i64
  %128 = getelementptr i8, ptr %74, i64 %112
  %129 = getelementptr i8, ptr %76, i64 %112
  %130 = getelementptr i8, ptr %129, i64 %120
  %131 = icmp ult i64 %111, 4
  %132 = and i64 %109, 3
  %133 = sub i64 %111, %132
  %134 = add i64 %105, %133
  %135 = icmp eq i64 %132, 0
  br label %141

136:                                              ; preds = %153
  %137 = add nuw nsw i64 %80, 16
  %138 = trunc i64 %137 to i32
  %139 = icmp sgt i32 %3, %138
  %140 = add i64 %79, 1
  br i1 %139, label %78, label %98, !llvm.loop !16

141:                                              ; preds = %158, %103
  %142 = phi i64 [ %161, %158 ], [ 0, %103 ]
  %143 = phi i64 [ %159, %158 ], [ %68, %103 ]
  %144 = mul i64 %32, %142
  %145 = getelementptr i8, ptr %128, i64 %144
  %146 = getelementptr i8, ptr %130, i64 %144
  %147 = mul nuw nsw i64 %143, %30
  %148 = getelementptr inbounds nuw double, ptr %0, i64 %147
  %149 = getelementptr inbounds nuw double, ptr %2, i64 %147
  %150 = icmp ult ptr %145, %123
  %151 = icmp ult ptr %121, %146
  %152 = and i1 %150, %151
  br label %162

153:                                              ; preds = %158
  %154 = add nuw nsw i64 %105, 16
  %155 = trunc i64 %154 to i32
  %156 = icmp sgt i32 %3, %155
  %157 = add i64 %104, 1
  br i1 %156, label %103, label %136, !llvm.loop !17

158:                                              ; preds = %190
  %159 = add nuw nsw i64 %143, 1
  %160 = icmp slt i64 %159, %73
  %161 = add i64 %142, 1
  br i1 %160, label %141, label %153, !llvm.loop !18

162:                                              ; preds = %190, %141
  %163 = phi i64 [ %80, %141 ], [ %191, %190 ]
  %164 = getelementptr inbounds nuw double, ptr %148, i64 %163
  %165 = load double, ptr %164, align 8, !tbaa !9
  %166 = mul nuw nsw i64 %163, %30
  %167 = getelementptr inbounds nuw double, ptr %1, i64 %166
  %168 = select i1 %131, i1 true, i1 %152
  br i1 %168, label %188, label %169

169:                                              ; preds = %162
  %170 = insertelement <2 x double> poison, double %165, i64 0
  %171 = shufflevector <2 x double> %170, <2 x double> poison, <2 x i32> zeroinitializer
  br label %172

172:                                              ; preds = %172, %169
  %173 = phi i64 [ 0, %169 ], [ %185, %172 ]
  %174 = add i64 %105, %173
  %175 = getelementptr inbounds nuw double, ptr %167, i64 %174
  %176 = getelementptr inbounds nuw i8, ptr %175, i64 16
  %177 = load <2 x double>, ptr %175, align 8, !tbaa !9, !alias.scope !19
  %178 = load <2 x double>, ptr %176, align 8, !tbaa !9, !alias.scope !19
  %179 = getelementptr inbounds nuw double, ptr %149, i64 %174
  %180 = getelementptr inbounds nuw i8, ptr %179, i64 16
  %181 = load <2 x double>, ptr %179, align 8, !tbaa !9, !alias.scope !22, !noalias !19
  %182 = load <2 x double>, ptr %180, align 8, !tbaa !9, !alias.scope !22, !noalias !19
  %183 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %171, <2 x double> %177, <2 x double> %181)
  %184 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %171, <2 x double> %178, <2 x double> %182)
  store <2 x double> %183, ptr %179, align 8, !tbaa !9, !alias.scope !22, !noalias !19
  store <2 x double> %184, ptr %180, align 8, !tbaa !9, !alias.scope !22, !noalias !19
  %185 = add nuw i64 %173, 4
  %186 = icmp eq i64 %185, %133
  br i1 %186, label %187, label %172, !llvm.loop !24

187:                                              ; preds = %172
  br i1 %135, label %190, label %188

188:                                              ; preds = %162, %187
  %189 = phi i64 [ %134, %187 ], [ %105, %162 ]
  br label %193

190:                                              ; preds = %193, %187
  %191 = add nuw nsw i64 %163, 1
  %192 = icmp slt i64 %191, %93
  br i1 %192, label %162, label %158, !llvm.loop !27

193:                                              ; preds = %188, %193
  %194 = phi i64 [ %200, %193 ], [ %189, %188 ]
  %195 = getelementptr inbounds nuw double, ptr %167, i64 %194
  %196 = load double, ptr %195, align 8, !tbaa !9
  %197 = getelementptr inbounds nuw double, ptr %149, i64 %194
  %198 = load double, ptr %197, align 8, !tbaa !9
  %199 = tail call double @llvm.fmuladd.f64(double %165, double %196, double %198)
  store double %199, ptr %197, align 8, !tbaa !9
  %200 = add nuw nsw i64 %194, 1
  %201 = icmp slt i64 %200, %127
  br i1 %201, label %193, label %190, !llvm.loop !28
}

; Function Attrs: mustprogress nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.fmuladd.f64(double, double, double) #1

; Function Attrs: nounwind sspstrong uwtable
define dso_local noundef i32 @main() local_unnamed_addr #2 {
  %1 = tail call noalias dereferenceable_or_null(32768) ptr @malloc(i64 noundef 32768) #10
  %2 = tail call noalias dereferenceable_or_null(32768) ptr @malloc(i64 noundef 32768) #10
  %3 = tail call noalias dereferenceable_or_null(32768) ptr @malloc(i64 noundef 32768) #10
  br label %4

4:                                                ; preds = %0, %122
  %5 = phi i64 [ 0, %0 ], [ %6, %122 ]
  %6 = add nuw nsw i64 %5, 1
  %7 = shl nuw nsw i64 %5, 6
  %8 = trunc nuw nsw i64 %6 to i32
  %9 = uitofp nneg i32 %8 to double
  %10 = insertelement <2 x i64> poison, i64 %5, i64 0
  %11 = shufflevector <2 x i64> %10, <2 x i64> poison, <2 x i32> zeroinitializer
  %12 = insertelement <2 x double> poison, double %9, i64 0
  %13 = shufflevector <2 x double> %12, <2 x double> poison, <2 x i32> zeroinitializer
  br label %14

14:                                               ; preds = %14, %4
  %15 = phi i64 [ 0, %4 ], [ %27, %14 ]
  %16 = phi <2 x i64> [ <i64 0, i64 1>, %4 ], [ %28, %14 ]
  %17 = add <2 x i64> %16, splat (i64 2)
  %18 = add nuw nsw i64 %15, %7
  %19 = getelementptr inbounds nuw double, ptr %1, i64 %18
  %20 = getelementptr inbounds nuw i8, ptr %19, i64 16
  store <2 x double> %13, ptr %19, align 8, !tbaa !9
  store <2 x double> %13, ptr %20, align 8, !tbaa !9
  %21 = icmp eq <2 x i64> %11, %16
  %22 = icmp eq <2 x i64> %11, %17
  %23 = select <2 x i1> %21, <2 x double> splat (double 1.000000e+00), <2 x double> zeroinitializer
  %24 = select <2 x i1> %22, <2 x double> splat (double 1.000000e+00), <2 x double> zeroinitializer
  %25 = getelementptr inbounds nuw double, ptr %2, i64 %18
  %26 = getelementptr inbounds nuw i8, ptr %25, i64 16
  store <2 x double> %23, ptr %25, align 8, !tbaa !9
  store <2 x double> %24, ptr %26, align 8, !tbaa !9
  %27 = add nuw i64 %15, 4
  %28 = add <2 x i64> %16, splat (i64 4)
  %29 = icmp eq i64 %27, 64
  br i1 %29, label %122, label %14, !llvm.loop !29

30:                                               ; preds = %124, %36
  %31 = phi i64 [ 16, %124 ], [ %39, %36 ]
  %32 = phi i64 [ 0, %124 ], [ %37, %36 ]
  br label %33

33:                                               ; preds = %49, %30
  %34 = phi i64 [ %52, %49 ], [ 16, %30 ]
  %35 = phi i64 [ %50, %49 ], [ 0, %30 ]
  br label %40

36:                                               ; preds = %49
  %37 = add nuw nsw i64 %32, 16
  %38 = icmp samesign ult i64 %32, 48
  %39 = add nuw nsw i64 %31, 16
  br i1 %38, label %30, label %125, !llvm.loop !15

40:                                               ; preds = %74, %33
  %41 = phi i64 [ 0, %33 ], [ %75, %74 ]
  %42 = or disjoint i64 %41, 2
  %43 = or disjoint i64 %41, 4
  %44 = or disjoint i64 %41, 6
  %45 = or disjoint i64 %41, 8
  %46 = or disjoint i64 %41, 10
  %47 = or disjoint i64 %41, 12
  %48 = or disjoint i64 %41, 14
  br label %53

49:                                               ; preds = %74
  %50 = add nuw nsw i64 %35, 16
  %51 = icmp samesign ult i64 %35, 48
  %52 = add nuw nsw i64 %34, 16
  br i1 %51, label %33, label %36, !llvm.loop !16

53:                                               ; preds = %77, %40
  %54 = phi i64 [ %32, %40 ], [ %78, %77 ]
  %55 = shl nuw nsw i64 %54, 6
  %56 = getelementptr inbounds nuw double, ptr %1, i64 %55
  %57 = getelementptr inbounds nuw double, ptr %3, i64 %55
  %58 = getelementptr inbounds nuw double, ptr %57, i64 %41
  %59 = getelementptr inbounds nuw double, ptr %57, i64 %42
  %60 = getelementptr inbounds nuw double, ptr %57, i64 %43
  %61 = getelementptr inbounds nuw double, ptr %57, i64 %44
  %62 = getelementptr inbounds nuw double, ptr %57, i64 %45
  %63 = getelementptr inbounds nuw double, ptr %57, i64 %46
  %64 = getelementptr inbounds nuw double, ptr %57, i64 %47
  %65 = getelementptr inbounds nuw double, ptr %57, i64 %48
  %66 = load <2 x double>, ptr %58, align 8, !tbaa !9
  %67 = load <2 x double>, ptr %59, align 8, !tbaa !9
  %68 = load <2 x double>, ptr %60, align 8, !tbaa !9
  %69 = load <2 x double>, ptr %61, align 8, !tbaa !9
  %70 = load <2 x double>, ptr %62, align 8, !tbaa !9
  %71 = load <2 x double>, ptr %63, align 8, !tbaa !9
  %72 = load <2 x double>, ptr %64, align 8, !tbaa !9
  %73 = load <2 x double>, ptr %65, align 8, !tbaa !9
  br label %80

74:                                               ; preds = %77
  %75 = add nuw nsw i64 %41, 16
  %76 = icmp samesign ult i64 %41, 48
  br i1 %76, label %40, label %49, !llvm.loop !17

77:                                               ; preds = %80
  store <2 x double> %98, ptr %58, align 8, !tbaa !9
  store <2 x double> %101, ptr %59, align 8, !tbaa !9
  store <2 x double> %104, ptr %60, align 8, !tbaa !9
  store <2 x double> %107, ptr %61, align 8, !tbaa !9
  store <2 x double> %110, ptr %62, align 8, !tbaa !9
  store <2 x double> %113, ptr %63, align 8, !tbaa !9
  store <2 x double> %116, ptr %64, align 8, !tbaa !9
  store <2 x double> %119, ptr %65, align 8, !tbaa !9
  %78 = add nuw nsw i64 %54, 1
  %79 = icmp eq i64 %78, %31
  br i1 %79, label %74, label %53, !llvm.loop !18

80:                                               ; preds = %80, %53
  %81 = phi i64 [ %35, %53 ], [ %120, %80 ]
  %82 = phi <2 x double> [ %66, %53 ], [ %98, %80 ]
  %83 = phi <2 x double> [ %67, %53 ], [ %101, %80 ]
  %84 = phi <2 x double> [ %68, %53 ], [ %104, %80 ]
  %85 = phi <2 x double> [ %69, %53 ], [ %107, %80 ]
  %86 = phi <2 x double> [ %70, %53 ], [ %110, %80 ]
  %87 = phi <2 x double> [ %71, %53 ], [ %113, %80 ]
  %88 = phi <2 x double> [ %72, %53 ], [ %116, %80 ]
  %89 = phi <2 x double> [ %73, %53 ], [ %119, %80 ]
  %90 = getelementptr inbounds nuw double, ptr %56, i64 %81
  %91 = load double, ptr %90, align 8, !tbaa !9
  %92 = shl nuw nsw i64 %81, 9
  %93 = getelementptr inbounds nuw i8, ptr %2, i64 %92
  %94 = getelementptr inbounds nuw double, ptr %93, i64 %41
  %95 = load <2 x double>, ptr %94, align 8, !tbaa !9
  %96 = insertelement <2 x double> poison, double %91, i64 0
  %97 = shufflevector <2 x double> %96, <2 x double> poison, <2 x i32> zeroinitializer
  %98 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %97, <2 x double> %95, <2 x double> %82)
  %99 = getelementptr inbounds nuw double, ptr %93, i64 %42
  %100 = load <2 x double>, ptr %99, align 8, !tbaa !9
  %101 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %97, <2 x double> %100, <2 x double> %83)
  %102 = getelementptr inbounds nuw double, ptr %93, i64 %43
  %103 = load <2 x double>, ptr %102, align 8, !tbaa !9
  %104 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %97, <2 x double> %103, <2 x double> %84)
  %105 = getelementptr inbounds nuw double, ptr %93, i64 %44
  %106 = load <2 x double>, ptr %105, align 8, !tbaa !9
  %107 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %97, <2 x double> %106, <2 x double> %85)
  %108 = getelementptr inbounds nuw double, ptr %93, i64 %45
  %109 = load <2 x double>, ptr %108, align 8, !tbaa !9
  %110 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %97, <2 x double> %109, <2 x double> %86)
  %111 = getelementptr inbounds nuw double, ptr %93, i64 %46
  %112 = load <2 x double>, ptr %111, align 8, !tbaa !9
  %113 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %97, <2 x double> %112, <2 x double> %87)
  %114 = getelementptr inbounds nuw double, ptr %93, i64 %47
  %115 = load <2 x double>, ptr %114, align 8, !tbaa !9
  %116 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %97, <2 x double> %115, <2 x double> %88)
  %117 = getelementptr inbounds nuw double, ptr %93, i64 %48
  %118 = load <2 x double>, ptr %117, align 8, !tbaa !9
  %119 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %97, <2 x double> %118, <2 x double> %89)
  %120 = add nuw nsw i64 %81, 1
  %121 = icmp eq i64 %120, %34
  br i1 %121, label %77, label %80, !llvm.loop !27

122:                                              ; preds = %14
  %123 = icmp eq i64 %6, 64
  br i1 %123, label %124, label %4, !llvm.loop !30

124:                                              ; preds = %122
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 8 dereferenceable(32768) %3, i8 0, i64 32768, i1 false), !tbaa !9
  br label %30

125:                                              ; preds = %36, %157
  %126 = phi i64 [ %158, %157 ], [ 0, %36 ]
  %127 = shl nuw nsw i64 %126, 6
  br label %160

128:                                              ; preds = %157
  %129 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  tail call void @free(ptr noundef nonnull %1) #11
  tail call void @free(ptr noundef %2) #11
  tail call void @free(ptr noundef nonnull %3) #11
  ret i32 0

130:                                              ; preds = %160
  %131 = or disjoint i64 %161, 1
  %132 = add nuw nsw i64 %131, %127
  %133 = getelementptr inbounds nuw double, ptr %3, i64 %132
  %134 = load double, ptr %133, align 8, !tbaa !9
  %135 = getelementptr inbounds nuw double, ptr %1, i64 %132
  %136 = load double, ptr %135, align 8, !tbaa !9
  %137 = fcmp oeq double %134, %136
  br i1 %137, label %138, label %168

138:                                              ; preds = %130
  %139 = or disjoint i64 %161, 2
  %140 = add nuw nsw i64 %139, %127
  %141 = getelementptr inbounds nuw double, ptr %3, i64 %140
  %142 = load double, ptr %141, align 8, !tbaa !9
  %143 = getelementptr inbounds nuw double, ptr %1, i64 %140
  %144 = load double, ptr %143, align 8, !tbaa !9
  %145 = fcmp oeq double %142, %144
  br i1 %145, label %146, label %168

146:                                              ; preds = %138
  %147 = or disjoint i64 %161, 3
  %148 = add nuw nsw i64 %147, %127
  %149 = getelementptr inbounds nuw double, ptr %3, i64 %148
  %150 = load double, ptr %149, align 8, !tbaa !9
  %151 = getelementptr inbounds nuw double, ptr %1, i64 %148
  %152 = load double, ptr %151, align 8, !tbaa !9
  %153 = fcmp oeq double %150, %152
  br i1 %153, label %154, label %168

154:                                              ; preds = %146
  %155 = add nuw nsw i64 %161, 4
  %156 = icmp eq i64 %155, 64
  br i1 %156, label %157, label %160, !llvm.loop !31

157:                                              ; preds = %154
  %158 = add nuw nsw i64 %126, 1
  %159 = icmp eq i64 %158, 64
  br i1 %159, label %128, label %125, !llvm.loop !32

160:                                              ; preds = %154, %125
  %161 = phi i64 [ 0, %125 ], [ %155, %154 ]
  %162 = add nuw nsw i64 %161, %127
  %163 = getelementptr inbounds nuw double, ptr %3, i64 %162
  %164 = load double, ptr %163, align 8, !tbaa !9
  %165 = getelementptr inbounds nuw double, ptr %1, i64 %162
  %166 = load double, ptr %165, align 8, !tbaa !9
  %167 = fcmp oeq double %164, %166
  br i1 %167, label %130, label %168

168:                                              ; preds = %146, %138, %130, %160
  tail call void @__assert_fail(ptr noundef nonnull @.str, ptr noundef nonnull @.str.1, i32 noundef 47, ptr noundef nonnull @__PRETTY_FUNCTION__.main) #12
  unreachable
}

; Function Attrs: mustprogress nofree nounwind willreturn allockind("alloc,uninitialized") allocsize(0) memory(inaccessiblemem: readwrite)
declare noalias noundef ptr @malloc(i64 noundef) local_unnamed_addr #3

; Function Attrs: cold noreturn nounwind
declare void @__assert_fail(ptr noundef, ptr noundef, i32 noundef, ptr noundef) local_unnamed_addr #4

; Function Attrs: mustprogress nounwind willreturn allockind("free") memory(argmem: readwrite, inaccessiblemem: readwrite)
declare void @free(ptr allocptr noundef captures(none)) local_unnamed_addr #5

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #6

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smin.i32(i32, i32) #7

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #8

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i64 @llvm.smin.i64(i64, i64) #7

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i64 @llvm.smax.i64(i64, i64) #7

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare <2 x double> @llvm.fmuladd.v2f64(<2 x double>, <2 x double>, <2 x double>) #7

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #9

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #2 = { nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nofree nounwind willreturn allockind("alloc,uninitialized") allocsize(0) memory(inaccessiblemem: readwrite) "alloc-family"="malloc" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { cold noreturn nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { mustprogress nounwind willreturn allockind("free") memory(argmem: readwrite, inaccessiblemem: readwrite) "alloc-family"="malloc" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #6 = { nofree nounwind }
attributes #7 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #8 = { nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #9 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }
attributes #10 = { nounwind allocsize(0) }
attributes #11 = { nounwind }
attributes #12 = { cold noreturn nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!10, !10, i64 0}
!10 = !{!"double", !7, i64 0}
!11 = distinct !{!11, !12}
!12 = !{!"llvm.loop.unroll.disable"}
!13 = distinct !{!13, !14}
!14 = !{!"llvm.loop.mustprogress"}
!15 = distinct !{!15, !14}
!16 = distinct !{!16, !14}
!17 = distinct !{!17, !14}
!18 = distinct !{!18, !14}
!19 = !{!20}
!20 = distinct !{!20, !21}
!21 = distinct !{!21, !"LVerDomain"}
!22 = !{!23}
!23 = distinct !{!23, !21}
!24 = distinct !{!24, !14, !25, !26}
!25 = !{!"llvm.loop.isvectorized", i32 1}
!26 = !{!"llvm.loop.unroll.runtime.disable"}
!27 = distinct !{!27, !14}
!28 = distinct !{!28, !14, !25}
!29 = distinct !{!29, !14, !25, !26}
!30 = distinct !{!30, !14}
!31 = distinct !{!31, !14}
!32 = distinct !{!32, !14}
