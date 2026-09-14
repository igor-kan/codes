; ModuleID = 'algorithms/02_c/graphs/lca_binary_lifting.c'
source_filename = "algorithms/02_c/graphs/lca_binary_lifting.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@depth = internal unnamed_addr global [100000 x i32] zeroinitializer, align 16
@up = internal unnamed_addr global [17 x [100000 x i32]] zeroinitializer, align 16
@head = internal unnamed_addr global [100000 x i32] zeroinitializer, align 16
@to = internal unnamed_addr global [200000 x i32] zeroinitializer, align 16
@next_e = internal unnamed_addr global [200000 x i32] zeroinitializer, align 16
@str = private unnamed_addr constant [36 x i8] c"[C LCA] Binary lifting LCA verified\00", align 1
@str.2 = private unnamed_addr constant [40 x i8] c"[C LCA] FAILED: binary lifting mismatch\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(read, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local i32 @lca(i32 noundef %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = sext i32 %0 to i64
  %4 = getelementptr inbounds i32, ptr @depth, i64 %3
  %5 = load i32, ptr %4, align 4, !tbaa !5
  %6 = sext i32 %1 to i64
  %7 = getelementptr inbounds i32, ptr @depth, i64 %6
  %8 = load i32, ptr %7, align 4, !tbaa !5
  %9 = icmp slt i32 %5, %8
  %10 = select i1 %9, i32 %0, i32 %1
  %11 = select i1 %9, i32 %1, i32 %0
  %12 = sext i32 %11 to i64
  %13 = getelementptr inbounds i32, ptr @depth, i64 %12
  %14 = load i32, ptr %13, align 4, !tbaa !5
  %15 = sext i32 %10 to i64
  %16 = getelementptr inbounds i32, ptr @depth, i64 %15
  %17 = load i32, ptr %16, align 4, !tbaa !5
  %18 = sub nsw i32 %14, %17
  br label %21

19:                                               ; preds = %33
  %20 = icmp eq i32 %34, %10
  br i1 %20, label %82, label %54

21:                                               ; preds = %47, %2
  %22 = phi i64 [ 0, %2 ], [ %49, %47 ]
  %23 = phi i32 [ %11, %2 ], [ %48, %47 ]
  %24 = trunc nuw nsw i64 %22 to i32
  %25 = shl nuw nsw i32 1, %24
  %26 = and i32 %25, %18
  %27 = icmp eq i32 %26, 0
  br i1 %27, label %33, label %28

28:                                               ; preds = %21
  %29 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %22
  %30 = sext i32 %23 to i64
  %31 = getelementptr inbounds i32, ptr %29, i64 %30
  %32 = load i32, ptr %31, align 4, !tbaa !5
  br label %33

33:                                               ; preds = %21, %28
  %34 = phi i32 [ %32, %28 ], [ %23, %21 ]
  %35 = or disjoint i64 %22, 1
  %36 = icmp eq i64 %22, 16
  br i1 %36, label %19, label %37, !llvm.loop !9

37:                                               ; preds = %33
  %38 = trunc nuw nsw i64 %35 to i32
  %39 = shl nuw nsw i32 1, %38
  %40 = and i32 %39, %18
  %41 = icmp eq i32 %40, 0
  br i1 %41, label %47, label %42

42:                                               ; preds = %37
  %43 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %35
  %44 = sext i32 %34 to i64
  %45 = getelementptr inbounds i32, ptr %43, i64 %44
  %46 = load i32, ptr %45, align 4, !tbaa !5
  br label %47

47:                                               ; preds = %42, %37
  %48 = phi i32 [ %46, %42 ], [ %34, %37 ]
  %49 = add nuw nsw i64 %22, 2
  br label %21

50:                                               ; preds = %54
  %51 = sext i32 %66 to i64
  %52 = getelementptr inbounds i32, ptr @up, i64 %51
  %53 = load i32, ptr %52, align 4, !tbaa !5
  br label %82

54:                                               ; preds = %19, %68
  %55 = phi i64 [ %81, %68 ], [ 16, %19 ]
  %56 = phi i32 [ %80, %68 ], [ %34, %19 ]
  %57 = phi i32 [ %79, %68 ], [ %10, %19 ]
  %58 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %55
  %59 = sext i32 %56 to i64
  %60 = getelementptr inbounds i32, ptr %58, i64 %59
  %61 = load i32, ptr %60, align 4, !tbaa !5
  %62 = sext i32 %57 to i64
  %63 = getelementptr inbounds i32, ptr %58, i64 %62
  %64 = load i32, ptr %63, align 4, !tbaa !5
  %65 = icmp eq i32 %61, %64
  %66 = select i1 %65, i32 %56, i32 %61
  %67 = icmp eq i64 %55, 0
  br i1 %67, label %50, label %68, !llvm.loop !11

68:                                               ; preds = %54
  %69 = select i1 %65, i32 %57, i32 %64
  %70 = getelementptr [100000 x i32], ptr @up, i64 %55
  %71 = getelementptr i8, ptr %70, i64 -400000
  %72 = sext i32 %66 to i64
  %73 = getelementptr inbounds i32, ptr %71, i64 %72
  %74 = load i32, ptr %73, align 4, !tbaa !5
  %75 = sext i32 %69 to i64
  %76 = getelementptr inbounds i32, ptr %71, i64 %75
  %77 = load i32, ptr %76, align 4, !tbaa !5
  %78 = icmp eq i32 %74, %77
  %79 = select i1 %78, i32 %69, i32 %77
  %80 = select i1 %78, i32 %66, i32 %74
  %81 = add nsw i64 %55, -2
  br label %54

82:                                               ; preds = %19, %50
  %83 = phi i32 [ %53, %50 ], [ %10, %19 ]
  ret i32 %83
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #1 {
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 16 dereferenceable(399984) getelementptr inbounds nuw (i8, ptr @head, i64 16), i8 -1, i64 399984, i1 false), !tbaa !5
  store <4 x i32> <i32 1, i32 0, i32 2, i32 0>, ptr @to, align 16, !tbaa !5
  store <4 x i32> <i32 -1, i32 -1, i32 0, i32 -1>, ptr @next_e, align 16, !tbaa !5
  store <4 x i32> <i32 3, i32 1, i32 4, i32 1>, ptr getelementptr inbounds nuw (i8, ptr @to, i64 16), align 16, !tbaa !5
  store <4 x i32> <i32 1, i32 -1, i32 4, i32 -1>, ptr getelementptr inbounds nuw (i8, ptr @next_e, i64 16), align 16, !tbaa !5
  store i32 7, ptr getelementptr inbounds nuw (i8, ptr @head, i64 16), align 16, !tbaa !5
  store i32 9, ptr getelementptr inbounds nuw (i8, ptr @head, i64 20), align 4, !tbaa !5
  store <4 x i32> <i32 2, i32 6, i32 10, i32 5>, ptr @head, align 16, !tbaa !5
  store <4 x i32> <i32 5, i32 2, i32 6, i32 2>, ptr getelementptr inbounds nuw (i8, ptr @to, i64 32), align 16, !tbaa !5
  store <4 x i32> <i32 3, i32 -1, i32 8, i32 -1>, ptr getelementptr inbounds nuw (i8, ptr @next_e, i64 32), align 16, !tbaa !5
  store i32 11, ptr getelementptr inbounds nuw (i8, ptr @head, i64 24), align 8, !tbaa !5
  store i32 0, ptr @depth, align 16, !tbaa !5
  tail call fastcc void @dfs(i32 noundef 0, i32 noundef -1)
  %1 = load i32, ptr getelementptr inbounds nuw (i8, ptr @depth, i64 12), align 4, !tbaa !5
  %2 = load i32, ptr getelementptr inbounds nuw (i8, ptr @depth, i64 16), align 16, !tbaa !5
  %3 = icmp slt i32 %1, %2
  %4 = select i1 %3, i32 3, i32 4
  %5 = select i1 %3, i32 4, i32 3
  %6 = zext nneg i32 %5 to i64
  %7 = getelementptr inbounds nuw i32, ptr @depth, i64 %6
  %8 = load i32, ptr %7, align 4, !tbaa !5
  %9 = zext nneg i32 %4 to i64
  %10 = getelementptr inbounds nuw i32, ptr @depth, i64 %9
  %11 = load i32, ptr %10, align 4, !tbaa !5
  %12 = sub nsw i32 %8, %11
  br label %15

13:                                               ; preds = %27
  %14 = icmp eq i32 %28, %4
  br i1 %14, label %231, label %44

15:                                               ; preds = %41, %0
  %16 = phi i64 [ 0, %0 ], [ %43, %41 ]
  %17 = phi i32 [ %5, %0 ], [ %42, %41 ]
  %18 = trunc nuw nsw i64 %16 to i32
  %19 = shl nuw nsw i32 1, %18
  %20 = and i32 %19, %12
  %21 = icmp eq i32 %20, 0
  br i1 %21, label %27, label %22

22:                                               ; preds = %15
  %23 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %16
  %24 = sext i32 %17 to i64
  %25 = getelementptr inbounds i32, ptr %23, i64 %24
  %26 = load i32, ptr %25, align 4, !tbaa !5
  br label %27

27:                                               ; preds = %22, %15
  %28 = phi i32 [ %26, %22 ], [ %17, %15 ]
  %29 = or disjoint i64 %16, 1
  %30 = icmp eq i64 %16, 16
  br i1 %30, label %13, label %31, !llvm.loop !9

31:                                               ; preds = %27
  %32 = trunc nuw nsw i64 %29 to i32
  %33 = shl nuw nsw i32 1, %32
  %34 = and i32 %33, %12
  %35 = icmp eq i32 %34, 0
  br i1 %35, label %41, label %36

36:                                               ; preds = %31
  %37 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %29
  %38 = sext i32 %28 to i64
  %39 = getelementptr inbounds i32, ptr %37, i64 %38
  %40 = load i32, ptr %39, align 4, !tbaa !5
  br label %41

41:                                               ; preds = %36, %31
  %42 = phi i32 [ %40, %36 ], [ %28, %31 ]
  %43 = add nuw nsw i64 %16, 2
  br label %15

44:                                               ; preds = %13, %58
  %45 = phi i64 [ %71, %58 ], [ 16, %13 ]
  %46 = phi i32 [ %70, %58 ], [ %28, %13 ]
  %47 = phi i32 [ %69, %58 ], [ %4, %13 ]
  %48 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %45
  %49 = sext i32 %46 to i64
  %50 = getelementptr inbounds i32, ptr %48, i64 %49
  %51 = load i32, ptr %50, align 4, !tbaa !5
  %52 = sext i32 %47 to i64
  %53 = getelementptr inbounds i32, ptr %48, i64 %52
  %54 = load i32, ptr %53, align 4, !tbaa !5
  %55 = icmp eq i32 %51, %54
  %56 = select i1 %55, i32 %46, i32 %51
  %57 = icmp eq i64 %45, 0
  br i1 %57, label %72, label %58, !llvm.loop !11

58:                                               ; preds = %44
  %59 = select i1 %55, i32 %47, i32 %54
  %60 = getelementptr [100000 x i32], ptr @up, i64 %45
  %61 = getelementptr i8, ptr %60, i64 -400000
  %62 = sext i32 %56 to i64
  %63 = getelementptr inbounds i32, ptr %61, i64 %62
  %64 = load i32, ptr %63, align 4, !tbaa !5
  %65 = sext i32 %59 to i64
  %66 = getelementptr inbounds i32, ptr %61, i64 %65
  %67 = load i32, ptr %66, align 4, !tbaa !5
  %68 = icmp eq i32 %64, %67
  %69 = select i1 %68, i32 %59, i32 %67
  %70 = select i1 %68, i32 %56, i32 %64
  %71 = add nsw i64 %45, -2
  br label %44

72:                                               ; preds = %44
  %73 = sext i32 %56 to i64
  %74 = getelementptr inbounds i32, ptr @up, i64 %73
  %75 = load i32, ptr %74, align 4, !tbaa !5
  %76 = icmp eq i32 %75, 1
  br i1 %76, label %77, label %231

77:                                               ; preds = %72
  %78 = load i32, ptr getelementptr inbounds nuw (i8, ptr @depth, i64 20), align 4, !tbaa !5
  %79 = icmp slt i32 %1, %78
  %80 = select i1 %79, i32 3, i32 5
  %81 = select i1 %79, i32 5, i32 3
  %82 = zext nneg i32 %81 to i64
  %83 = getelementptr inbounds nuw i32, ptr @depth, i64 %82
  %84 = load i32, ptr %83, align 4, !tbaa !5
  %85 = zext nneg i32 %80 to i64
  %86 = getelementptr inbounds nuw i32, ptr @depth, i64 %85
  %87 = load i32, ptr %86, align 4, !tbaa !5
  %88 = sub nsw i32 %84, %87
  br label %91

89:                                               ; preds = %103
  %90 = icmp eq i32 %104, %80
  br i1 %90, label %231, label %120

91:                                               ; preds = %117, %77
  %92 = phi i64 [ 0, %77 ], [ %119, %117 ]
  %93 = phi i32 [ %81, %77 ], [ %118, %117 ]
  %94 = trunc nuw nsw i64 %92 to i32
  %95 = shl nuw nsw i32 1, %94
  %96 = and i32 %95, %88
  %97 = icmp eq i32 %96, 0
  br i1 %97, label %103, label %98

98:                                               ; preds = %91
  %99 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %92
  %100 = sext i32 %93 to i64
  %101 = getelementptr inbounds i32, ptr %99, i64 %100
  %102 = load i32, ptr %101, align 4, !tbaa !5
  br label %103

103:                                              ; preds = %98, %91
  %104 = phi i32 [ %102, %98 ], [ %93, %91 ]
  %105 = or disjoint i64 %92, 1
  %106 = icmp eq i64 %92, 16
  br i1 %106, label %89, label %107, !llvm.loop !9

107:                                              ; preds = %103
  %108 = trunc nuw nsw i64 %105 to i32
  %109 = shl nuw nsw i32 1, %108
  %110 = and i32 %109, %88
  %111 = icmp eq i32 %110, 0
  br i1 %111, label %117, label %112

112:                                              ; preds = %107
  %113 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %105
  %114 = sext i32 %104 to i64
  %115 = getelementptr inbounds i32, ptr %113, i64 %114
  %116 = load i32, ptr %115, align 4, !tbaa !5
  br label %117

117:                                              ; preds = %112, %107
  %118 = phi i32 [ %116, %112 ], [ %104, %107 ]
  %119 = add nuw nsw i64 %92, 2
  br label %91

120:                                              ; preds = %89, %134
  %121 = phi i64 [ %147, %134 ], [ 16, %89 ]
  %122 = phi i32 [ %146, %134 ], [ %104, %89 ]
  %123 = phi i32 [ %145, %134 ], [ %80, %89 ]
  %124 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %121
  %125 = sext i32 %122 to i64
  %126 = getelementptr inbounds i32, ptr %124, i64 %125
  %127 = load i32, ptr %126, align 4, !tbaa !5
  %128 = sext i32 %123 to i64
  %129 = getelementptr inbounds i32, ptr %124, i64 %128
  %130 = load i32, ptr %129, align 4, !tbaa !5
  %131 = icmp eq i32 %127, %130
  %132 = select i1 %131, i32 %122, i32 %127
  %133 = icmp eq i64 %121, 0
  br i1 %133, label %148, label %134, !llvm.loop !11

134:                                              ; preds = %120
  %135 = select i1 %131, i32 %123, i32 %130
  %136 = getelementptr [100000 x i32], ptr @up, i64 %121
  %137 = getelementptr i8, ptr %136, i64 -400000
  %138 = sext i32 %132 to i64
  %139 = getelementptr inbounds i32, ptr %137, i64 %138
  %140 = load i32, ptr %139, align 4, !tbaa !5
  %141 = sext i32 %135 to i64
  %142 = getelementptr inbounds i32, ptr %137, i64 %141
  %143 = load i32, ptr %142, align 4, !tbaa !5
  %144 = icmp eq i32 %140, %143
  %145 = select i1 %144, i32 %135, i32 %143
  %146 = select i1 %144, i32 %132, i32 %140
  %147 = add nsw i64 %121, -2
  br label %120

148:                                              ; preds = %120
  %149 = sext i32 %132 to i64
  %150 = getelementptr inbounds i32, ptr @up, i64 %149
  %151 = load i32, ptr %150, align 4, !tbaa !5
  %152 = icmp eq i32 %151, 0
  br i1 %152, label %153, label %231

153:                                              ; preds = %148
  %154 = load i32, ptr getelementptr inbounds nuw (i8, ptr @depth, i64 24), align 8, !tbaa !5
  %155 = icmp slt i32 %78, %154
  %156 = select i1 %155, i32 5, i32 6
  %157 = select i1 %155, i32 6, i32 5
  %158 = zext nneg i32 %157 to i64
  %159 = getelementptr inbounds nuw i32, ptr @depth, i64 %158
  %160 = load i32, ptr %159, align 4, !tbaa !5
  %161 = zext nneg i32 %156 to i64
  %162 = getelementptr inbounds nuw i32, ptr @depth, i64 %161
  %163 = load i32, ptr %162, align 4, !tbaa !5
  %164 = sub nsw i32 %160, %163
  br label %167

165:                                              ; preds = %179
  %166 = icmp eq i32 %180, %156
  br i1 %166, label %231, label %196

167:                                              ; preds = %193, %153
  %168 = phi i64 [ 0, %153 ], [ %195, %193 ]
  %169 = phi i32 [ %157, %153 ], [ %194, %193 ]
  %170 = trunc nuw nsw i64 %168 to i32
  %171 = shl nuw nsw i32 1, %170
  %172 = and i32 %171, %164
  %173 = icmp eq i32 %172, 0
  br i1 %173, label %179, label %174

174:                                              ; preds = %167
  %175 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %168
  %176 = sext i32 %169 to i64
  %177 = getelementptr inbounds i32, ptr %175, i64 %176
  %178 = load i32, ptr %177, align 4, !tbaa !5
  br label %179

179:                                              ; preds = %174, %167
  %180 = phi i32 [ %178, %174 ], [ %169, %167 ]
  %181 = or disjoint i64 %168, 1
  %182 = icmp eq i64 %168, 16
  br i1 %182, label %165, label %183, !llvm.loop !9

183:                                              ; preds = %179
  %184 = trunc nuw nsw i64 %181 to i32
  %185 = shl nuw nsw i32 1, %184
  %186 = and i32 %185, %164
  %187 = icmp eq i32 %186, 0
  br i1 %187, label %193, label %188

188:                                              ; preds = %183
  %189 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %181
  %190 = sext i32 %180 to i64
  %191 = getelementptr inbounds i32, ptr %189, i64 %190
  %192 = load i32, ptr %191, align 4, !tbaa !5
  br label %193

193:                                              ; preds = %188, %183
  %194 = phi i32 [ %192, %188 ], [ %180, %183 ]
  %195 = add nuw nsw i64 %168, 2
  br label %167

196:                                              ; preds = %165, %210
  %197 = phi i64 [ %223, %210 ], [ 16, %165 ]
  %198 = phi i32 [ %222, %210 ], [ %180, %165 ]
  %199 = phi i32 [ %221, %210 ], [ %156, %165 ]
  %200 = getelementptr inbounds nuw [100000 x i32], ptr @up, i64 %197
  %201 = sext i32 %198 to i64
  %202 = getelementptr inbounds i32, ptr %200, i64 %201
  %203 = load i32, ptr %202, align 4, !tbaa !5
  %204 = sext i32 %199 to i64
  %205 = getelementptr inbounds i32, ptr %200, i64 %204
  %206 = load i32, ptr %205, align 4, !tbaa !5
  %207 = icmp eq i32 %203, %206
  %208 = select i1 %207, i32 %198, i32 %203
  %209 = icmp eq i64 %197, 0
  br i1 %209, label %224, label %210, !llvm.loop !11

210:                                              ; preds = %196
  %211 = select i1 %207, i32 %199, i32 %206
  %212 = getelementptr [100000 x i32], ptr @up, i64 %197
  %213 = getelementptr i8, ptr %212, i64 -400000
  %214 = sext i32 %208 to i64
  %215 = getelementptr inbounds i32, ptr %213, i64 %214
  %216 = load i32, ptr %215, align 4, !tbaa !5
  %217 = sext i32 %211 to i64
  %218 = getelementptr inbounds i32, ptr %213, i64 %217
  %219 = load i32, ptr %218, align 4, !tbaa !5
  %220 = icmp eq i32 %216, %219
  %221 = select i1 %220, i32 %211, i32 %219
  %222 = select i1 %220, i32 %208, i32 %216
  %223 = add nsw i64 %197, -2
  br label %196

224:                                              ; preds = %196
  %225 = sext i32 %208 to i64
  %226 = getelementptr inbounds i32, ptr @up, i64 %225
  %227 = load i32, ptr %226, align 4, !tbaa !5
  %228 = icmp ne i32 %227, 2
  %229 = select i1 %228, ptr @str.2, ptr @str
  %230 = zext i1 %228 to i32
  br label %231

231:                                              ; preds = %224, %72, %148, %13, %89, %165
  %232 = phi ptr [ @str.2, %72 ], [ @str.2, %165 ], [ @str.2, %89 ], [ @str.2, %13 ], [ %229, %224 ], [ @str.2, %148 ]
  %233 = phi i32 [ 1, %72 ], [ 1, %165 ], [ 1, %89 ], [ 1, %13 ], [ %230, %224 ], [ 1, %148 ]
  %234 = tail call i32 @puts(ptr nonnull dereferenceable(1) %232)
  ret i32 %233
}

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define internal fastcc void @dfs(i32 noundef %0, i32 noundef %1) unnamed_addr #2 {
  %3 = sext i32 %0 to i64
  %4 = getelementptr inbounds i32, ptr @up, i64 %3
  store i32 %1, ptr %4, align 4, !tbaa !5
  %5 = icmp eq i32 %1, -1
  br i1 %5, label %6, label %10

6:                                                ; preds = %2
  %7 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 400000), i64 %3
  store i32 -1, ptr %7, align 4, !tbaa !5
  br label %16

8:                                                ; preds = %132
  %9 = getelementptr inbounds i32, ptr @depth, i64 %3
  br label %139

10:                                               ; preds = %2
  %11 = sext i32 %1 to i64
  %12 = getelementptr inbounds i32, ptr @up, i64 %11
  %13 = load i32, ptr %12, align 4, !tbaa !5
  %14 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 400000), i64 %3
  store i32 %13, ptr %14, align 4, !tbaa !5
  %15 = icmp eq i32 %13, -1
  br i1 %15, label %16, label %18

16:                                               ; preds = %10, %6
  %17 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 800000), i64 %3
  store i32 -1, ptr %17, align 4, !tbaa !5
  br label %24

18:                                               ; preds = %10
  %19 = sext i32 %13 to i64
  %20 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 400000), i64 %19
  %21 = load i32, ptr %20, align 4, !tbaa !5
  %22 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 800000), i64 %3
  store i32 %21, ptr %22, align 4, !tbaa !5
  %23 = icmp eq i32 %21, -1
  br i1 %23, label %24, label %26

24:                                               ; preds = %18, %16
  %25 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 1200000), i64 %3
  store i32 -1, ptr %25, align 4, !tbaa !5
  br label %32

26:                                               ; preds = %18
  %27 = sext i32 %21 to i64
  %28 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 800000), i64 %27
  %29 = load i32, ptr %28, align 4, !tbaa !5
  %30 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 1200000), i64 %3
  store i32 %29, ptr %30, align 4, !tbaa !5
  %31 = icmp eq i32 %29, -1
  br i1 %31, label %32, label %34

32:                                               ; preds = %26, %24
  %33 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 1600000), i64 %3
  store i32 -1, ptr %33, align 4, !tbaa !5
  br label %40

34:                                               ; preds = %26
  %35 = sext i32 %29 to i64
  %36 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 1200000), i64 %35
  %37 = load i32, ptr %36, align 4, !tbaa !5
  %38 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 1600000), i64 %3
  store i32 %37, ptr %38, align 4, !tbaa !5
  %39 = icmp eq i32 %37, -1
  br i1 %39, label %40, label %42

40:                                               ; preds = %34, %32
  %41 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2000000), i64 %3
  store i32 -1, ptr %41, align 4, !tbaa !5
  br label %48

42:                                               ; preds = %34
  %43 = sext i32 %37 to i64
  %44 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 1600000), i64 %43
  %45 = load i32, ptr %44, align 4, !tbaa !5
  %46 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2000000), i64 %3
  store i32 %45, ptr %46, align 4, !tbaa !5
  %47 = icmp eq i32 %45, -1
  br i1 %47, label %48, label %50

48:                                               ; preds = %42, %40
  %49 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2400000), i64 %3
  store i32 -1, ptr %49, align 4, !tbaa !5
  br label %56

50:                                               ; preds = %42
  %51 = sext i32 %45 to i64
  %52 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2000000), i64 %51
  %53 = load i32, ptr %52, align 4, !tbaa !5
  %54 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2400000), i64 %3
  store i32 %53, ptr %54, align 4, !tbaa !5
  %55 = icmp eq i32 %53, -1
  br i1 %55, label %56, label %58

56:                                               ; preds = %50, %48
  %57 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2800000), i64 %3
  store i32 -1, ptr %57, align 4, !tbaa !5
  br label %64

58:                                               ; preds = %50
  %59 = sext i32 %53 to i64
  %60 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2400000), i64 %59
  %61 = load i32, ptr %60, align 4, !tbaa !5
  %62 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2800000), i64 %3
  store i32 %61, ptr %62, align 4, !tbaa !5
  %63 = icmp eq i32 %61, -1
  br i1 %63, label %64, label %66

64:                                               ; preds = %58, %56
  %65 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 3200000), i64 %3
  store i32 -1, ptr %65, align 4, !tbaa !5
  br label %72

66:                                               ; preds = %58
  %67 = sext i32 %61 to i64
  %68 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 2800000), i64 %67
  %69 = load i32, ptr %68, align 4, !tbaa !5
  %70 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 3200000), i64 %3
  store i32 %69, ptr %70, align 4, !tbaa !5
  %71 = icmp eq i32 %69, -1
  br i1 %71, label %72, label %74

72:                                               ; preds = %66, %64
  %73 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 3600000), i64 %3
  store i32 -1, ptr %73, align 4, !tbaa !5
  br label %80

74:                                               ; preds = %66
  %75 = sext i32 %69 to i64
  %76 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 3200000), i64 %75
  %77 = load i32, ptr %76, align 4, !tbaa !5
  %78 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 3600000), i64 %3
  store i32 %77, ptr %78, align 4, !tbaa !5
  %79 = icmp eq i32 %77, -1
  br i1 %79, label %80, label %82

80:                                               ; preds = %74, %72
  %81 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4000000), i64 %3
  store i32 -1, ptr %81, align 4, !tbaa !5
  br label %88

82:                                               ; preds = %74
  %83 = sext i32 %77 to i64
  %84 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 3600000), i64 %83
  %85 = load i32, ptr %84, align 4, !tbaa !5
  %86 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4000000), i64 %3
  store i32 %85, ptr %86, align 4, !tbaa !5
  %87 = icmp eq i32 %85, -1
  br i1 %87, label %88, label %90

88:                                               ; preds = %82, %80
  %89 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4400000), i64 %3
  store i32 -1, ptr %89, align 4, !tbaa !5
  br label %96

90:                                               ; preds = %82
  %91 = sext i32 %85 to i64
  %92 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4000000), i64 %91
  %93 = load i32, ptr %92, align 4, !tbaa !5
  %94 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4400000), i64 %3
  store i32 %93, ptr %94, align 4, !tbaa !5
  %95 = icmp eq i32 %93, -1
  br i1 %95, label %96, label %98

96:                                               ; preds = %90, %88
  %97 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4800000), i64 %3
  store i32 -1, ptr %97, align 4, !tbaa !5
  br label %104

98:                                               ; preds = %90
  %99 = sext i32 %93 to i64
  %100 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4400000), i64 %99
  %101 = load i32, ptr %100, align 4, !tbaa !5
  %102 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4800000), i64 %3
  store i32 %101, ptr %102, align 4, !tbaa !5
  %103 = icmp eq i32 %101, -1
  br i1 %103, label %104, label %106

104:                                              ; preds = %98, %96
  %105 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 5200000), i64 %3
  store i32 -1, ptr %105, align 4, !tbaa !5
  br label %112

106:                                              ; preds = %98
  %107 = sext i32 %101 to i64
  %108 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 4800000), i64 %107
  %109 = load i32, ptr %108, align 4, !tbaa !5
  %110 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 5200000), i64 %3
  store i32 %109, ptr %110, align 4, !tbaa !5
  %111 = icmp eq i32 %109, -1
  br i1 %111, label %112, label %114

112:                                              ; preds = %106, %104
  %113 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 5600000), i64 %3
  store i32 -1, ptr %113, align 4, !tbaa !5
  br label %120

114:                                              ; preds = %106
  %115 = sext i32 %109 to i64
  %116 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 5200000), i64 %115
  %117 = load i32, ptr %116, align 4, !tbaa !5
  %118 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 5600000), i64 %3
  store i32 %117, ptr %118, align 4, !tbaa !5
  %119 = icmp eq i32 %117, -1
  br i1 %119, label %120, label %122

120:                                              ; preds = %114, %112
  %121 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 6000000), i64 %3
  store i32 -1, ptr %121, align 4, !tbaa !5
  br label %132

122:                                              ; preds = %114
  %123 = sext i32 %117 to i64
  %124 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 5600000), i64 %123
  %125 = load i32, ptr %124, align 4, !tbaa !5
  %126 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 6000000), i64 %3
  store i32 %125, ptr %126, align 4, !tbaa !5
  %127 = icmp eq i32 %125, -1
  br i1 %127, label %132, label %128

128:                                              ; preds = %122
  %129 = sext i32 %125 to i64
  %130 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 6000000), i64 %129
  %131 = load i32, ptr %130, align 4, !tbaa !5
  br label %132

132:                                              ; preds = %120, %128, %122
  %133 = phi i32 [ %131, %128 ], [ -1, %122 ], [ -1, %120 ]
  %134 = getelementptr inbounds i32, ptr getelementptr inbounds nuw (i8, ptr @up, i64 6400000), i64 %3
  store i32 %133, ptr %134, align 4, !tbaa !5
  %135 = getelementptr inbounds i32, ptr @head, i64 %3
  %136 = load i32, ptr %135, align 4, !tbaa !5
  %137 = icmp eq i32 %136, -1
  br i1 %137, label %138, label %8

138:                                              ; preds = %150, %132
  ret void

139:                                              ; preds = %8, %150
  %140 = phi i32 [ %136, %8 ], [ %152, %150 ]
  %141 = sext i32 %140 to i64
  %142 = getelementptr inbounds i32, ptr @to, i64 %141
  %143 = load i32, ptr %142, align 4, !tbaa !5
  %144 = icmp eq i32 %143, %1
  br i1 %144, label %150, label %145

145:                                              ; preds = %139
  %146 = load i32, ptr %9, align 4, !tbaa !5
  %147 = add nsw i32 %146, 1
  %148 = sext i32 %143 to i64
  %149 = getelementptr inbounds i32, ptr @depth, i64 %148
  store i32 %147, ptr %149, align 4, !tbaa !5
  tail call fastcc void @dfs(i32 noundef %143, i32 noundef %0)
  br label %150

150:                                              ; preds = %139, %145
  %151 = getelementptr inbounds i32, ptr @next_e, i64 %141
  %152 = load i32, ptr %151, align 4, !tbaa !5
  %153 = icmp eq i32 %152, -1
  br i1 %153, label %138, label %139, !llvm.loop !12
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #3

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(read, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nosync nounwind sspstrong memory(readwrite, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind }
attributes #4 = { nocallback nofree nounwind willreturn memory(argmem: write) }

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
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
!11 = distinct !{!11, !10}
!12 = distinct !{!12, !10}
